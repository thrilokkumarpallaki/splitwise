import enum

from . import *


class ExpenseType(enum.Enum):
    EXPENSE = 1
    TRANSACTION = 2


class ExpenseModel(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(NUMERIC(10, 2), nullable=False)
    description = Column(String(100), nullable=True)
    expense_type = Column(Enum(ExpenseType), nullable=False)
    user = Column(Integer, ForeignKey('users.id'), nullable=True)
    group = Column(Integer, ForeignKey('groups.id'), nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    last_modified_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())



