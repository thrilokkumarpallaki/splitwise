from exceptions import GroupDoesNotExist, UnauthorizedAccessException, UserNotFoundException
from models.group_model import GroupModel
from models.user_model import UserModel
from models.user_group_mapping_model import UserGroupMappingModel


class GroupView:
    @staticmethod
    def create_group(**kwargs):
        user_id = kwargs.get('user_id')
        group_name = kwargs.get('group_name')

        # Create Group
        group_obj = GroupModel(name=group_name, created_by=user_id)
        group_id = group_obj.save()

        # Add admin to the group
        user_group_mapping_obj = UserGroupMappingModel(user_id=user_id, group_id=group_id)
        user_group_mapping_obj.save()

        if group_id is not None:
            return 'SUCCESS'
        return 'FAILED'

    @staticmethod
    def add_member(**kwargs):
        admin_id = kwargs.get('admin_id')
        group_id = kwargs.get('group_id')
        user_id = kwargs.get('user_id')

        # Check if the admin id is actual admin of the group
        group_obj = GroupModel.get_group(group_id)
        if group_obj is None:
            raise GroupDoesNotExist("Group does not exist!")

        if group_obj.created_by != int(admin_id):
            raise UnauthorizedAccessException()

        # Add member to the group
        user_group_mapping_obj = UserGroupMappingModel(user_id=user_id, group_id=group_id)
        status = user_group_mapping_obj.save()

        if status:
            return 'SUCCESS'
        return 'FAILED'

    @staticmethod
    def show_groups(**kwargs):
        user_groups = {}
        user_id = kwargs.get('user_id')

        # get the user object along with groups if the user is present
        user_obj = UserModel.get_user(user_id)

        if user_obj is None:
            raise UserNotFoundException()
        
        for group in user_obj.groups:
            group_name = group.name
            group_description = group.description
            user_groups[group_name] = group_description
        return user_groups
