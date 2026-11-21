"""Number base conversion helpers."""


def to_bases(number: int) -> str:
    """Return a non-negative integer as binary, octal and hexadecimal.

    Example:
        to_bases(255) returns "0b11111111 0o377 0xff".

    Raises:
        ValueError: if number is negative.
    """
    if number < 0:
        raise ValueError("Error: only non-negative integers are supported")
    return f"{bin(number)} {oct(number)} {hex(number)}"
