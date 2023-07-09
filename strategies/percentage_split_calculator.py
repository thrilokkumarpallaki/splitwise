from functools import reduce

from app.strategies.isplit_calculator import ISplitCalculator
from app.models.expense_model import ExpenseModel, ExpenseType
from app.models.user_expense_model import UserExpenseModel, UserExpenseType


class PercentageSplitCalculator(ISplitCalculator):
    def __init__(self, total_amount: float, paid_by: int):
        self.total_amount = total_amount
        self.paid_by = paid_by

    def create_split(self, *, percentages: dict = None,
                     group_id: int = None,
                     description: str = None) -> tuple[ExpenseModel, list[UserExpenseModel]]:
        # Check if total amount is distributed completely
        def percentage_sum_cal(percent, percentage_sum=0):
            percentage_sum += (self.total_amount / 100) * percent
            return percentage_sum

