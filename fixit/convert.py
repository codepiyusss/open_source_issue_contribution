"""Unit conversions."""

KM_PER_MILE = 1.609344
LBS_PER_KG = 2.20462
ABSOLUTE_ZERO_CELSIUS = -273.15
ABSOLUTE_ZERO_FAHRENHEIT = -459.67


def celsius_to_fahrenheit(c: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Example:
        celsius_to_fahrenheit(0) returns 32.
    """
    if c < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError("temperature cannot be below absolute zero")
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius.

    Example:
        fahrenheit_to_celsius(32) returns 0.
    """
    if f < ABSOLUTE_ZERO_FAHRENHEIT:
        raise ValueError("temperature cannot be below absolute zero")
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    """Convert a temperature from Celsius to Kelvin.

    Raises ValueError if the result would be below absolute zero.

    Example:
        celsius_to_kelvin(0) returns 273.15.
    """
    kelvin = c + 273.15
    if kelvin < 0:
        raise ValueError("temperature cannot be below absolute zero (0 K)")
    return kelvin


def kelvin_to_celsius(k: float) -> float:
    """Convert a temperature from Kelvin to Celsius.

    Raises ValueError if the Kelvin value is negative.

    Example:
        kelvin_to_celsius(273.15) returns 0.
    """
    if k < 0:
        raise ValueError("Kelvin value cannot be negative")
    return k - 273.15


def km_to_miles(km: float) -> float:
    """Convert kilometers to miles.

    Example:
        km_to_miles(1) returns approximately 0.6214.
    """
    return km / KM_PER_MILE


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometers.

    Example:
        miles_to_km(1) returns approximately 1.6093.
    """
    return miles * KM_PER_MILE


def kg_to_lbs(kg: float) -> float:
    """Convert kilograms to pounds.

    Example:
        kg_to_lbs(1) returns approximately 2.20462.
    """
    return kg * LBS_PER_KG


def lbs_to_kg(lbs: float) -> float:
    """Convert pounds to kilograms.

    Example:
        lbs_to_kg(2.20462) returns approximately 1.
    """
    return lbs / LBS_PER_KG
