import pytest

from fixit.roman import from_roman, to_roman


# --- to_roman: normal and edge cases ---

def test_to_roman_1994():
    assert to_roman(1994) == "MCMXCIV"


def test_to_roman_smallest():
    assert to_roman(1) == "I"            # what is 1 in Roman?


def test_to_roman_largest():
    assert to_roman(3999) == "MMMCMXCIX"         # the biggest Roman numeral (you saw it earlier)


def test_to_roman_rejects_zero():
    with pytest.raises(ValueError):
        to_roman(0)                    # just below the allowed range


def test_to_roman_rejects_4000():
    with pytest.raises(ValueError):
        to_roman(4000)                    # just above the allowed range


# --- from_roman: normal and edge cases ---

def test_from_roman_1994():
    assert from_roman("MCMXCIV") == 1994  # the number


def test_from_roman_lowercase():
    assert from_roman("mcmxciv") == 1994       # same numeral, in lowercase letters


def test_from_roman_rejects_four_in_a_row():
    with pytest.raises(ValueError):
        from_roman("IIII")                  # 4 written the WRONG way (4 of the same letter)


def test_from_roman_rejects_bad_pair():
    with pytest.raises(ValueError):
        from_roman("IC")


def test_from_roman_rejects_empty():
    with pytest.raises(ValueError):
        from_roman("")                  # an empty string


def test_from_roman_rejects_letters():
    with pytest.raises(ValueError):
        from_roman("ABC")