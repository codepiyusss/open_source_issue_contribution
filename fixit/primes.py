"""Prime number checking utilities."""


def is_prime(number: int) -> bool:
    """Return True if number is prime, otherwise False.

    Args:
        number: Integer to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    divisor = 3

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False

        divisor += 2

    return True