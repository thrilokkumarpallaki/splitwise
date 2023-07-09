from flask import Blueprint

from app.views.group_view import GroupView

groups_api = Blueprint("groups_api", __name__, url_prefix='/groups')


def create_group(**kwargs):
    user_id = kwargs.get('user_id')
    group_name = kwargs.get('group_name')
    return GroupView.create_group(user_id=user_id, group_name=group_name)


def add_member(**kwargs):
    admin_id = kwargs.get('admin_id')
    group_id = kwargs.get('group_id')
    user_id = kwargs.get('user_id')
    return GroupView.add_member(admin_id=admin_id, group_id=group_id, user_id=user_id)


def show_groups(**kwargs):
    user_id = kwargs.get('user_id')
    return GroupView.show_groups(user_id=user_id)
