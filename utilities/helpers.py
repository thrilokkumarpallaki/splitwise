from flask_bcrypt import generate_password_hash


def encrypt_password(password_text: str) -> str:
    """
    This helper function is used to encrypt the given password text.
    :param password_text: Password to generate the hash
    :return: It returns encrypted hash
    """
    encrypted_pass = generate_password_hash(password_text, 10).decode('utf-8')
    return encrypted_pass
