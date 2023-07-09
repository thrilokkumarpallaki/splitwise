from . import *


class UserGroupMappingModel(Base):
    __tablename__ = 'user_group_mappings'
    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'group_id'),
    )

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)

    def save(self):
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
