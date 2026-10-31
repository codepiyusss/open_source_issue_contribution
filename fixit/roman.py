"""Roman numeral conversion module with validation."""

def to_roman(n: int) -> str:
    """Convert an integer to a Roman numeral (1 to 3999)."""
    if not isinstance(n, int) or not (1 <= n <= 3999):
        raise ValueError("Input must be an integer between 1 and 3999")
    
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num

def from_roman(s: str) -> int:
    """Convert a Roman numeral string to an integer."""
    if not isinstance(s, str):
        raise ValueError("Input must be a string not a valid Roman numeral")
    
    # Normalize to uppercase to support lowercase inputs like 'mcmxciv'
    s = s.upper()
    
    # Check for invalid characters or basic structural violations
    import re
    # Pattern to validate standard Roman numerals from 1 to 3999
    pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    if not re.match(pattern, s):
        raise ValueError(f"'{s}' is not a valid Roman numeral")
        
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and roman_map[s[i]] > roman_map[s[i - 1]]:
            int_val += roman_map[s[i]] - 2 * roman_map[s[i - 1]]
        else:
            int_val += roman_map[s[i]]
    return int_val