from . import *


class GroupModel(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(String(100), nullable=True)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    last_modified_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    @staticmethod
    def get_group(group_id: int):
        session = Session()
        group_obj = None

        try:
            group_obj = session.query(GroupModel).filter(GroupModel.id == group_id).first()
        except Exception as e:
            print(e)
        finally:
            session.close()
        return group_obj

    def save(self):
        session = Session()
        group_id = None
        try:
            session.add(self)
            session.commit()
            group_id = self.id
        except Exception as e:
            print(e)
        finally:
            session.close()
        return group_id
