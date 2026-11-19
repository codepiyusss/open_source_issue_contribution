"""FizzBuzz sequence generator."""

from __future__ import annotations


def fizzbuzz(n: int) -> list[str]:
    """Return the FizzBuzz sequence from 1 to n inclusive.

    Multiples of 3 and 5 become "FizzBuzz", multiples of 3 become "Fizz",
    multiples of 5 become "Buzz", and other numbers become their string form.
    Raises ValueError if n is less than 1.
    """
    if n < 1:
        raise ValueError("n must be at least 1")

    result: list[str] = []
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))
    return result