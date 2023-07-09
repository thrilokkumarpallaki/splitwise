"""
This is a concrete command class to create/ register the user
"""
from . import *
from controllers.user_controller import create_user


class RegisterUserCommand(ICommand):
    @classmethod
    def match(cls, *, cmd_input: str) -> bool:
        cmd_input_split = cmd_input.split(" ")
        if len(cmd_input_split) == 4 and cmd_input_split[0].lower() == Commands.REGISTER.lower():
            return True
        return False

    @classmethod
    def execute(cls, cmd_input: str):
        cmd_input_split = cmd_input.split(" ")
        name = cmd_input_split[1]
        phone = cmd_input_split[2]
        password = cmd_input_split[3]
