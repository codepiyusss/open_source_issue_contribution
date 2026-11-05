import pytest

from fixit.convert import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
    km_to_miles,
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


def test_c_to_k():
    assert celsius_to_kelvin(0) == pytest.approx(273.15)


def test_k_to_c():
    assert kelvin_to_celsius(273.15) == pytest.approx(0)


def test_c_to_k_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        celsius_to_kelvin(-300)


def test_k_to_c_negative_raises():
    with pytest.raises(ValueError):
        kelvin_to_celsius(-1)


def test_temperature_conversions_reject_below_absolute_zero_and_accept_boundary():
    with pytest.raises(ValueError):
        celsius_to_fahrenheit(-273.150001)
    assert celsius_to_fahrenheit(-273.15) == pytest.approx(-459.67)
    assert celsius_to_fahrenheit(-273.149999) == pytest.approx(-459.6699982)

    with pytest.raises(ValueError):
        fahrenheit_to_celsius(-459.670001)
    assert fahrenheit_to_celsius(-459.67) == pytest.approx(-273.15)
    assert fahrenheit_to_celsius(-459.669999) == pytest.approx(-273.1499994444)
