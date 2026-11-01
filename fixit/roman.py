"""Roman numeral conversion for numbers 1 to 3999."""

_VALUES = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def to_roman(number: int) -> str:
    """Convert an integer from 1 to 3999 to a Roman numeral.

    >>> to_roman(1994)
    'MCMXCIV'
    """
    if isinstance(number, bool) or not isinstance(number, int) or not 1 <= number <= 3999:
        raise ValueError("number must be an integer from 1 to 3999")
    result = []
    for value, symbol in _VALUES:
        while number >= value:
            result.append(symbol)
            number -= value
    return "".join(result)


def from_roman(text: str) -> int:
    """Convert a valid Roman numeral to an integer.

    >>> from_roman('MCMXCIV')
    1994
    """
    s = str(text).strip().upper()
    index = 0
    total = 0
    for value, symbol in _VALUES:
        while s.startswith(symbol, index):
            total += value
            index += len(symbol)
    if not s or index != len(s) or total == 0 or to_roman(total) != s:
        raise ValueError(f"Invalid Roman numeral: {text!r}")
    return total