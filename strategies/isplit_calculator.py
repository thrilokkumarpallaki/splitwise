from abc import ABC, abstractmethod

from app.models.expense_model import ExpenseModel
from app.models.user_expense_model import UserExpenseModel


class ISplitCalculator(ABC):
    @abstractmethod
    def create_split(self, **kwargs) -> tuple[ExpenseModel, list[UserExpenseModel]]:
        pass
