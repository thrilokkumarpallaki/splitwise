"""
User business logic
"""
from app.models.user_model import UserModel, UserStatus
from app.exceptions import UserCreationException, UserNotFoundException
from app.utilities.helpers import encrypt_password


class UserView:
    """
    The purpose of the view is to create/update users in the application.
    """
    @staticmethod
    def create_user(**kwargs):
        """
        This method helps in creating the user with the given
        details. If already user exists with the given information.
        Instead of creating a new user it updates the status of the user
        to ACTIVE otherwise, nothing.
        :param kwargs: It takes keyword arguments to create the user.
        :return: None
        """

        name = kwargs.get('name')
        phone = kwargs.get('phone')
        password = kwargs.get('password')

        user_obj = UserModel.get_user(phone)

        if user_obj is not None:
            # User exist
            user_obj.name = name
            user_obj.password = password
            user_obj.status = UserStatus.ACTIVE
        else:
            encrypted_password = encrypt_password(password)
            # Create user
            user_obj = UserModel(name=name, phone=phone, password=encrypted_password, status=UserStatus.ACTIVE)
        create_status = user_obj.save()

        if not create_status:
            raise UserCreationException("Something went wrong. User not created!", 5000)
        return "SUCCESS"

    @staticmethod
    def update_user(**kwargs):
        """
        This method is to update the user's password.
        :param kwargs: new password of the user.
        :return: None
        """
        user_id = kwargs.get('user_id')
        new_password = kwargs.get('password')

        user_obj = UserModel.get_user(user_id)

        if user_obj is not None:
            # Generate password hash
            encrypted_password = encrypt_password(new_password)
            user_obj.password = encrypted_password
            user_obj.save()
        else:
            raise UserNotFoundException()
        return "SUCCESS"
