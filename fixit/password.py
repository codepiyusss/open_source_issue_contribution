"""Random password generator."""

import random
import string


def generate(
    length: int = 12, use_digits: bool = True, use_symbols: bool = False
) -> str:
    """Generate a random password of the given length.

    Example:
        generate(4, use_digits=False) returns a 4-character password.
    """
    if length <= 0:
        raise ValueError("Password length must be greater then 0!")
    chars = string.digits
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return "".join(random.choice(chars) for _ in range(length))
