from app.models.expense_model import ExpenseModel
from app.strategies.isplit_calculator import ISplitCalculator
from app.strategies.equal_split_calculator import EqualSplitCalculator
from app.strategies.exact_split_calculator import ExactSplitCalculator


class ExpenseView:
    @staticmethod
    def create_expense(**kwargs):
        user_id = kwargs.get('user_id')
        group_id = kwargs.get('group_id')
        payers = kwargs.get('payers', [])
        user_ids = kwargs.get('user_ids', [])
        split_type = kwargs.get('split_type')
        desc = kwargs.get('desc')

        