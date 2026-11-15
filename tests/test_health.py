"""Tests for BMI calculation."""

import pytest

from fixit.health import calculate_bmi


def test_calculate_bmi():
    assert round(calculate_bmi(70, 175), 1) == 22.9


def test_invalid_inputs():
    with pytest.raises(ValueError):
        calculate_bmi(0, 175)

    with pytest.raises(ValueError):
        calculate_bmi(70, -175)