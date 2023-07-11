from app.strategies.isplit_calculator import ISplitCalculator
from app.exceptions import EqualSplitException
from app.models.expense_model import ExpenseModel, ExpenseType
from app.models.user_expense_model import UserExpenseModel, UserExpenseType


class EqualSplitCalculator(ISplitCalculator):
    def __init__(self, total_amount: float, paid_by: int, multi_payers: dict = None):
        self.total_amount = total_amount
        self.paid_by = paid_by
        self.multi_payers = multi_payers

    def create_split(self, *,
                     users: list = None,
                     group_id: int = None,
                     description: str = None) -> ExpenseModel:
        # Get the length of the users
        no_of_users = len(users)

        if no_of_users == 0:
            raise EqualSplitException("At least two users are required to equally share the expense!")

        amount_per_share = self.total_amount / no_of_users

        expense_obj = ExpenseModel(amount=self.total_amount,
                                   description=description,
                                   expense_type=ExpenseType.EXPENSE,
                                   # Assuming paid by user is adding expense
                                   # In case of multiple payers the first
                                   created_by=self.paid_by,
                                   group=group_id)

        user_expenses = []
        for user in users:
            user_expense_obj = UserExpenseModel(user=user,
                                                expense=expense_obj.id,
                                                amount=amount_per_share,
                                                user_expense_type=UserExpenseType.HAD_TO_PAY)
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
