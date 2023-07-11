from functools import reduce

from .isplit_calculator import ISplitCalculator
from app.exceptions import ExactSplitMisMatchException
from app.models.expense_model import ExpenseModel, ExpenseType
from app.models.user_expense_model import UserExpenseModel, UserExpenseType


class ExactSplitCalculator(ISplitCalculator):
    def __init__(self, total_amount: float, paid_by: int, multi_payers: dict = None):
        self.total_amount = total_amount
        self.paid_by = paid_by
        self.multi_payers = multi_payers
        
    def create_split(self, *,
                     users: dict,
                     description: str,
                     group_id: int) -> ExpenseModel:
        # Check if the exact_amount sum is matching with total_amount
        exact_sum = reduce(lambda x, y: x + y, users.values())

        if self.total_amount != exact_sum:
            raise ExactSplitMisMatchException("Exact shares between users not matching with total amount.")
        
        # create Expense Object
        expense_obj = ExpenseModel(amount=self.total_amount,
                                   description=description,
                                   expense_type=ExpenseType.EXPENSE,
                                   created_by=self.paid_by,
                                   group=group_id)

        user_expenses = []
        for user, amount in users.items():
            user_expense_obj = UserExpenseModel(amount=amount,
                                                user=user,
                                                expense=expense_obj.id,
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
