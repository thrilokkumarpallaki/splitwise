import re

from flask_bcrypt import generate_password_hash

from app.exceptions import InvalidInputFormatException, DuplicateUserException


def encrypt_password(password_text: str) -> str:
    """
    This helper function is used to encrypt the given password text.
    :param password_text: Password to generate the hash
    :return: It returns encrypted hash
    """
    encrypted_pass = generate_password_hash(password_text, 10).decode('utf-8')
    return encrypted_pass


def split_equal_share_users(payees: str) -> list[int]:
    """
    This is a helper function to split the users.
    :param payees: A Str object with space separated payees
    :return: A list of int objects
    """
    payees = payees.strip()
    payees_list = list(map(int, payees.split(' ')))
    return payees_list


def split_other_share_users(payees: str) -> dict[str: float]:
    """
    This is a helper function to split the user from their share of value
    in the expense. This function generates a dict of user as key and share
    as value.
    :param payees: A Str object with space separated payees and associated with their shares.
    :return: A dict
    """
    payees = payees.strip()
    pattern = re.compile(r'\d+:\d+\s')
    if re.match(pattern, payees) is None:
        raise InvalidInputFormatException('Invalid format for payees!')
    else:
        payees_dict = {}
        payees_split = payees.split(' ')

        for payee in payees_split:
            payee = payee.strip()
            user, share = payee.split(':')
            user = str(user).strip()
            share = str(share).strip()

            if user not in payees_dict:
                payees_dict[user] = float(share)
            else:
                raise DuplicateUserException('User is repeated more than one time in the payees list!')
    return payees_dict


def multi_payers_split(payers: str) -> dict[str, float]:
    """
    This is a helper function to split the payers from their contributed share in
    the expense.
    :param payers: A Str object with space separated payers and associated with their shares.
    :return: A dict
    """
    payers = payers.strip()
    pattern = re.compile(r'\d+:\d+\s')
    if re.match(pattern, payers) is None:
        raise InvalidInputFormatException('Invalid format for payers!')
    else:
        payers_dict = {}
        payers_split = payers.split(' ')

        for payee in payers_split:
            payee = payee.strip()
            user, share = payee.split(':')
            user = str(user).strip()
            share = str(share).strip()

            if user not in payers_dict:
                payers_dict[user] = float(share)
            else:
                raise DuplicateUserException('User is repeated more than one time in the payers list!')
    return payers_dict
