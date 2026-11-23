import pytest
from hypothesis import given, strategies as st

from fixit.convert import celsius_to_fahrenheit, fahrenheit_to_celsius
from fixit.wordcount import count_chars


@given(
    celsius=st.floats(
        min_value=-273.15,
        max_value=1e6,
        allow_nan=False,
        allow_infinity=False,
    )
)
def test_celsius_fahrenheit_round_trip(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    converted_back = fahrenheit_to_celsius(fahrenheit)

    assert converted_back == pytest.approx(celsius, abs=1e-6)


@given(first=st.text(), second=st.text())
def test_count_chars_is_additive(first, second):
    assert count_chars(first + second) == count_chars(first) + count_chars(second)
