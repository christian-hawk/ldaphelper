import string
import random

def get_random_inum():
    """[Generates a fake random inum, aplhanumeric 30 digits]

    Returns:
        [str]: [30 digit alphanumeric string to be used as inum]
    """
    letters_and_digits = string.ascii_letters + string.digits
    fake_inum = ''.join((random.choice(letters_and_digits) for i in range(30)))
    return fake_inum
