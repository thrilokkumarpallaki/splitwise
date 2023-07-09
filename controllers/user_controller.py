from flask import Blueprint

from app.views.user_view import UserView

user_api = Blueprint('user_api', __name__, url_prefix='/users')


def create_user(**kwargs):
    """
    User creation api.
    :return:
    """
    name = kwargs.get('name')
    phone = kwargs.get('phone')
    password = kwargs.get('password')
    return UserView.create_user(name=name, phone=phone, password=password)


def update_user(**kwargs):
    """
    User update api.
    :return:
    """
    user_id = kwargs.get('user_id')
    new_password = kwargs.get('password')
    return UserView.update_user(user_id=user_id, password=new_password)
