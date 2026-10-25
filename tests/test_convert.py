import pytest

from fixit.convert import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kg_to_lbs,
    km_to_miles,
    lbs_to_kg,
    miles_to_km,
)


def test_c_to_f():
    assert celsius_to_fahrenheit(100) == 212


def test_f_to_c():
    assert fahrenheit_to_celsius(32) == 0


def test_km_to_miles():
    assert km_to_miles(10) == pytest.approx(6.21371, rel=1e-4)


def test_miles_to_km():
    assert miles_to_km(1) == pytest.approx(1.609344)


def test_negative_celsius():
    assert celsius_to_fahrenheit(-20) == -4


def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == 32


def test_absolute_zero():
    assert celsius_to_fahrenheit(-273.15) == pytest.approx(-459.67)


def test_float_km_to_miles():
    assert km_to_miles(1.5) == pytest.approx(0.932056788)


def test_kg_to_lbs():
    assert kg_to_lbs(1) == pytest.approx(2.20462)
    assert kg_to_lbs(10) == pytest.approx(22.0462)


def test_lbs_to_kg():
    assert lbs_to_kg(2.20462) == pytest.approx(1.0)
    assert lbs_to_kg(10) == pytest.approx(4.53592, rel=1e-3)

