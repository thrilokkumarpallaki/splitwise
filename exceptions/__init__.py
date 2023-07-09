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
    Raised when an equal split calculator has issues users belonging to the expnse.
    """
    err_msg = 'No users to share the split error!'
    err_status = 400

    def __init__(self, err_msg: str = None, err_status: int = None):
        self.err_msg = err_msg
        self.err_status = err_status