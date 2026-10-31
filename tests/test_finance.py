"""Tests for loan EMI calculation."""

import pytest

from fixit.finance import calculate_emi


def test_calculate_emi():
    """Test EMI calculation with a regular interest rate."""
    assert calculate_emi(500000, 8.5, 5) == pytest.approx(10258.27, abs=0.01)


def test_calculate_emi_zero_interest():
    """Test EMI calculation when there is no interest."""
    assert calculate_emi(12000, 0, 1) == 1000


def test_calculate_emi_invalid_principal():
    """Test that zero or negative principal is rejected."""
    with pytest.raises(ValueError):
        calculate_emi(0, 8.5, 5)


def test_calculate_emi_negative_interest():
    """Test that negative interest is rejected."""
    with pytest.raises(ValueError):
        calculate_emi(500000, -1, 5)


def test_calculate_emi_invalid_years():
    """Test that zero or negative loan duration is rejected."""
    with pytest.raises(ValueError):
        calculate_emi(500000, 8.5, 0)