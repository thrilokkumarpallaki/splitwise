import enum

from . import *
from .user_expense_model import UserExpenseModel


class ExpenseType(enum.Enum):
    EXPENSE = 1
    TRANSACTION = 2


class ExpenseModel(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(NUMERIC(10, 2), nullable=False)
    description = Column(String(100), nullable=True)
    expense_type = Column(Enum(ExpenseType), nullable=False)
    # To whom amount is paid
    user = Column(Integer, ForeignKey('users.id'), nullable=True)
    group = Column(Integer, ForeignKey('groups.id'), nullable=True)
    # Who paid the amount
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    last_modified_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    user_expenses = relationship('UserExpenseModel', uselist=True)

    def save(self):
        session = Session(expire_on_commit=True)
        status = False
        try:
            session.add(self)
            session.commit()
            status = True
        except Exception as e:
            print(e)
        finally:
            session.close()
        return status

    def delete(self):
        session = Session()
        status = False
        try:
            session.delete(self)
            session.commit()
            session.refresh(self)
            status = True
        except Exception as e:
            print(e)
        finally:
            session.close()
        return status
