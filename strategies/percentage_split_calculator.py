from app.exceptions import PercentageSplitException
from app.strategies.isplit_calculator import ISplitCalculator
from app.models.expense_model import ExpenseModel, ExpenseType
from app.models.user_expense_model import UserExpenseModel, UserExpenseType


class PercentageSplitCalculator(ISplitCalculator):
    def __init__(self, total_amount: float, paid_by: int, multi_payers: dict = None):
        self.total_amount = total_amount
        self.paid_by = paid_by
        self.multi_payers = multi_payers

    def create_split(self, *, users: dict = None,
                     group_id: int = None,
                     description: str = None) -> ExpenseModel:

        # Check if total amount is distributed completely
        def percentage_sum_cal(percent, percentage_sum=0):
            percentage_sum += (self.total_amount / 100) * percent
            return percentage_sum

        ps = 0

        for prcnt in users.values():
            ps = percentage_sum_cal(prcnt, ps)

        if ps != self.total_amount:
            raise PercentageSplitException('Percentage share is not matching with total amount!')

        expense_obj = ExpenseModel(amount=self.total_amount,
                                   description=description,
                                   expense_type=ExpenseType.EXPENSE,
                                   group=group_id,
                                   created_by=self.paid_by)

        user_expenses = []

        for user, prcnt in users.items():
            share_amount = (self.total_amount / 100) * prcnt

            user_expense_obj = UserExpenseModel(user=user,
                                                expense=expense_obj.id,
                                                user_expense_type=UserExpenseType.HAD_TO_PAY,
                                                amount=share_amount)
            user_expenses.append(user_expense_obj)

        if self.multi_payers is not None and len(self.multi_payers) > 0:
            for payer, amount in self.multi_payers.items():
                user_expense_obj = UserExpenseModel(user=payer,
                                                    expense=expense_obj.id,
                                                    amount=amount,
                                                    user_expense_type=UserExpenseType.PAID)
                user_expenses.append(user_expense_obj)
        else:
            user_expense_obj = UserExpenseModel(user=self.paid_by,
                                                expense=expense_obj.id,
                                                amount=self.total_amount,
                                                user_expense_type=UserExpenseType.PAID)
            user_expenses.append(user_expense_obj)
        expense_obj.user_expenses.extend(user_expenses)

        return expense_obj
