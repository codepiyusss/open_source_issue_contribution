import pytest

from fixit.roman import from_roman, to_roman


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, "I"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (3999, "MMMCMXCIX"),
    ],
)
def test_to_roman_values(number, expected):
    assert to_roman(number) == expected


@pytest.mark.parametrize(
    ("numeral", "expected"),
    [
        ("I", 1),
        ("IV", 4),
        ("mcmxciv", 1994),
        ("mmmdccclxxxviii", 3888),
    ],
)
def test_from_roman_values(numeral, expected):
    assert from_roman(numeral) == expected


@pytest.mark.parametrize("value", [0, -1, 4000])
def test_to_roman_rejects_out_of_range(value):
    with pytest.raises(ValueError, match="between 1 and 3999"):
        to_roman(value)


@pytest.mark.parametrize("numeral", ["IIII", "VX", "IC", "MMMM", "ABC"])
def test_from_roman_rejects_invalid_numerals(numeral):
    with pytest.raises(ValueError, match="not a valid Roman numeral"):
        from_roman(numeral)
