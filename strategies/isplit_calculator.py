from abc import ABC, abstractmethod

from app.models.expense_model import ExpenseModel


class ISplitCalculator(ABC):
    @abstractmethod
    def create_split(self, **kwargs) -> ExpenseModel:
        pass
