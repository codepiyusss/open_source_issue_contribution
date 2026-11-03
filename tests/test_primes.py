"""Tests for prime number checking."""

from fixit.primes import is_prime


def test_prime_numbers():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(29) is True


def test_non_prime_numbers():
    assert is_prime(4) is False
    assert is_prime(28) is False
    assert is_prime(9) is False


def test_edge_cases():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-5) is False