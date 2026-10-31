ROMAN_VALUES = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]

def to_roman(number: int) -> str:

    """Convert an integer from 1 to 3999 to a Roman numeral."""

    if number < 1 or number > 3999:
        raise ValueError("Error: number must be between 0 and 1000")

    result = ""
    for value, symbol in ROMAN_VALUES:
        while number >= value:
            result += symbol
            number -= value
    return result

def from_roman(numeral: str) -> int:
    """Convert a Roman numeral to an integer."""

    text = numeral.upper()
    total = 0
    pos = 0
    for value, symbol in ROMAN_VALUES:
        while text.startswith(symbol, pos):   
            total += value                     
            pos += len(symbol)                  
    if total == 0 or to_roman(total) != text:   
        raise ValueError(f"Error: '{numeral}' is not a valid Roman numeral")
    return total   