"""Unit conversions."""

KM_PER_MILE = 1.609344


def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def km_to_miles(km: float) -> float:
    return km / KM_PER_MILE


def miles_to_km(miles: float) -> float:
    return miles * KM_PER_MILE
