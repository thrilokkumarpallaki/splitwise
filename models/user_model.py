"""
User database logic
"""

from __future__ import annotations

from app.enums.user_status_type import UserStatusType
from . import *


class UserModel(Base):
    """
    UserModel mapped to User table in the DB.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    phone = Column(String(10), nullable=False, unique=True)
    password = Column(String(60), nullable=True)
    status = Column(Enum(UserStatusType), default=UserStatusType.INVITED)
    groups = relationship('GroupModel', back_populates="members", uselist=True,
                          secondary='user_group_mappings', lazy='joined')
    created_at = Column(DateTime(timezone=True), default=func.now())
    last_modified_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    @staticmethod
    def get_user(user_id: int = None, phone_number: str = None) -> UserModel | None:
        """
        This method helps to get the user record from the database.
        :param user_id: primary key of the user
        :param phone_number: A user phone number
        :return: It returns user_object if user is present otherwise, None.
        """
        session = Session()
        user_obj = None

        try:
            base_query = session.query(UserModel)
            if user_id is not None:
                user_obj = base_query.filter(UserModel.id == user_id).first()
            else:
                user_obj = base_query.filter(UserModel.phone == phone_number).first()
        except Exception as e:
            print(e)
        finally:
            session.close()
        return user_obj

    def save(self) -> bool:
        """
        It saves user current user object.
        :return: None
        """
        session = Session()
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
