from .equal_split_calculator import EqualSplitCalculator
from .exact_split_calculator import ExactSplitCalculator
from .percentage_split_calculator import PercentageSplitCalculator
from .ratio_split_calculator import RatioSplitCalculator
from .isplit_calculator import ISplitCalculator
from app.models.expense_model import ExpenseModel
from app.enums.split_type import SplitType


class SplitCalculateContext:
    def __init__(self, calculator: ISplitCalculator):
        self.calculator = calculator

    def calculate_split(self, **kwargs) -> ExpenseModel:
        return self.calculator.create_split(**kwargs)


def delegate_expense(split_type, total_amount, paid_by, multi_payers):
    calculator = None
    if split_type == SplitType.EQUAL_SPLIT:
        calculator = EqualSplitCalculator(total_amount, paid_by, multi_payers)
    elif split_type == SplitType.EXACT_SPLIT:
        calculator = ExactSplitCalculator(total_amount, paid_by, multi_payers)
    elif split_type == SplitType.PERCENTAGE_SPLIT:
        calculator = PercentageSplitCalculator(total_amount, paid_by, multi_payers)
    elif split_type == SplitType.RATIO_SPLIT:
        calculator = RatioSplitCalculator(total_amount, paid_by, multi_payers)
    return SplitCalculateContext(calculator)
