"""
Exceptions for Application
"""


class UserCreationException(Exception):
    """
    Raised when creation user is not successful
    """
    err_msg = ''
    err_status = None

    def __init__(self, err_msg, err_status):
        self.err_msg = err_msg
        self.err_status = err_status


class UserNotFoundException(Exception):
    """
    Raised when a user does not exist.
    """
    err_msg = 'User does not exist!'
    err_status = 404

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status


class GroupDoesNotExist(Exception):
    """
    Raised when a group does not exist.
    """
    err_msg = "Group does not exist!"
    err_status = 404

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status


class GroupAlreadyExistsException(Exception):
    """
    Raised when a user creates a group with name already exists.
    """
    err_msg = "Group already exists"
    err_statu = 400

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status


class UnauthorizedAccessException(Exception):
    """
    Raised when an unauthorized user tries to access the group.
    """
    err_msg = 'Unauthorized access!'
    err_status = 401

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status


class ExactSplitMisMatchException(Exception):
    """
    Raised when an exact split is not matching between the total amount
    and exact shares between users
    """
    err_msg = 'Exact shares mismatch error!'
    err_status = 400

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status


class EqualSplitException(Exception):
    """
    Raised when an equal split calculator has issues users belonging to the expense.
    """
    err_msg = 'No users to share the split error!'
    err_status = 400

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status


class PercentageSplitException(Exception):
    """
    Raised when sum of all percentage is not equal to zero
    """
    err_msg = 'Percentages share is not equal to the total amount entered'
    err_status = 400

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status


class InvalidInputFormatException(Exception):
    """
    Raised when an input is not given properly.
    """
    err_msg = 'Input format is not correct!'
    err_status = 400

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status


class DuplicateUserException(Exception):
    """
    Raised when a user is repeated multiple types in the Payees option.
    """
    err_msg = "User share is repeated more than once!"
    err_statsu = 400

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status


class UsersNotBelongToGroup(Exception):
    err_msg = "One or more users not belong to the group!"
    err_statsu = 400

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status


class ExpenseException(Exception):
    err_msg = "Expense creator must be part of payees and payers"
    err_status = 400

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status
