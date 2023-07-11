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

    @staticmethod
    def check_for_users(group_id, users):
        session = Session()
        status = False
        try:
            map_recs = session.query(UserGroupMappingModel)\
                .filter(UserGroupMappingModel.group_id == group_id)\
                .filter(UserGroupMappingModel.user_id.in_(users)).all()

            if len(users) == len(map_recs):
                status = True
        except Exception as e:
            print(e)
        finally:
            session.close()
        return status
