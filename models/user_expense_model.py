import enum

from . import *


class UserExpenseType(enum.Enum):
    PAID = 1
    HAD_TO_PAY = 2


class UserExpenseModel(Base):
    __tablename__ = 'user_expenses'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'), nullable=False)
    expense = Column(Integer, ForeignKey('expenses.id'), nullable=False)
    user_expense_type = Column(Enum(UserExpenseType), nullable=False)
    amount = Column(NUMERIC(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    last_modified_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
