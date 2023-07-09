from app.strategies.isplit_calculator import ISplitCalculator
from app.exceptions import EqualSplitException
from app.models.expense_model import ExpenseModel, ExpenseType
from app.models.user_expense_model import UserExpenseModel, UserExpenseType


class EqualSplitCalculator(ISplitCalculator):
    def __init__(self, total_amount: float, paid_by: int, multi_payers: list):
        self.total_amount = total_amount
        self.paid_by = paid_by
        self.multi_payers = multi_payers

    def create_split(self, *, users: list = None, group_id: int = None, description: str = None) -> tuple[ExpenseModel, list[UserExpenseModel]]:
        # Get the length of the users
        no_of_users = len(users)

        if no_of_users == 0:
            raise EqualSplitException("At least two user is required to exactly share the expense!")

        amount_per_share = self.total_amount / no_of_users

        # create Expense object
        expense_obj = ExpenseModel(amount=self.total_amount,
                                   description=description,
                                   expense_type=ExpenseType.EXPENSE,
                                   user=self.paid_by,
                                   group=group_id)

        user_expenses = []
        for user in users:
            user_expense_obj = UserExpenseModel(user=user,
                                                expense=expense_obj.id,
                                                amount=amount_per_share)

            user_expenses.append(user_expense_obj)
        return expense_obj, user_expenses
