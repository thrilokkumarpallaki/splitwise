from functools import reduce

from .isplit_calculator import ISplitCalculator
from app.exceptions import ExactSplitMisMatchException
from app.models.expense_model import ExpenseModel, ExpenseType
from app.models.user_expense_model import UserExpenseModel, UserExpenseType


class ExactSplitCalculator(ISplitCalculator):
    def __init__(self, total_amount: float, paid_by: int):
        self.total_amount = total_amount
        self.paid_by = paid_by
        
    def create_split(self, *, exact_amount: dict, description: str) -> tuple[ExpenseModel, list[UserExpenseModel]]:
        # Check if the exact_amount sum is matching with total_amount
        exact_sum = reduce(lambda x, y: x + y, exact_amount.values())

        if self.total_amount != exact_sum:
            raise ExactSplitMisMatchException("Exact shares between users not matching with toatal amount.")
        
        # create Expense Object
        expense_obj = ExpenseModel(amount=self.total_amount,
                                   description=description,
                                   expense_type=ExpenseType.EXPENSE,
                                   user=self.paid_by)

        user_expenses = []
        for user, amount in exact_amount.items():
            user_expense_obj = UserExpenseModel(amount=amount,
                                                description=description,
                                                user=user,
                                                expense=expense_obj.id)

            if self.paid_by == user:
                user_expense_obj.expense_type = UserExpenseType.PAID
            else:
                user_expense_obj.expense_type = UserExpenseType.HAD_TO_PAY

            user_expenses.append(user_expense_obj)
        return expense_obj, user_expenses
        