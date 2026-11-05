import random

import pytest

from fixit.cli import main
from fixit.coin import flip


def test_flip_defaults_to_one_result():
    assert len(flip()) == 1


def test_flip_returns_requested_count():
    assert len(flip(5)) == 5


def test_flip_only_returns_heads_or_tails():
    results = flip(100, random.Random(1))
    assert set(results) <= {"Heads", "Tails"}


def test_flip_rejects_zero():
    with pytest.raises(ValueError):
        flip(0)


def test_coin_command_prints_one_line_per_flip(capsys):
    result = main(["coin", "--count", "3"])

    lines = capsys.readouterr().out.splitlines()
    assert result == 0
    assert len(lines) == 3


def test_flip_same_seed_gives_same_results():
    first = flip(20, random.Random(42))
    second = flip(20, random.Random(42))
    assert first == second


def test_flip_can_return_both_sides():
    results = flip(100, random.Random(1))
    assert set(results) == {"Heads", "Tails"}


def test_flip_rejects_negative_count():
    with pytest.raises(ValueError):
        flip(-1)


def test_coin_command_defaults_to_one_line(capsys):
    result = main(["coin"])

    lines = capsys.readouterr().out.splitlines()
    assert result == 0
    assert len(lines) == 1


def test_coin_command_rejects_zero(capsys):
    result = main(["coin", "--count", "0"])

    assert result == 1
    assert "at least 1" in capsys.readouterr().err


def test_coin_command_rejects_negative_count(capsys):
    result = main(["coin", "--count", "-1"])

    assert result == 1
    assert "at least 1" in capsys.readouterr().err


def test_coin_command_rejects_non_integer_count():
    with pytest.raises(SystemExit) as exc_info:
        main(["coin", "--count", "abc"])

    assert exc_info.value.code == 2
