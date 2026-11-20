import pytest

from fixit.cli import main
from fixit.fizzbuzz import fizzbuzz


def test_fizzbuzz_normal_fifteen():
    assert fizzbuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]


def test_fizzbuzz_single_element():
    assert fizzbuzz(1) == ["1"]


def test_fizzbuzz_rejects_zero():
    with pytest.raises(ValueError, match="at least 1"):
        fizzbuzz(0)


def test_fizzbuzz_rejects_negative():
    with pytest.raises(ValueError, match="at least 1"):
        fizzbuzz(-5)


def test_fizzbuzz_command_prints_lines(capsys):
    code = main(["fizzbuzz", "5"])
    captured = capsys.readouterr()

    assert code == 0
    assert captured.out.splitlines() == ["1", "2", "Fizz", "4", "Buzz"]
    assert captured.err == ""


def test_fizzbuzz_command_rejects_less_than_one(capsys):
    code = main(["fizzbuzz", "0"])
    captured = capsys.readouterr()

    assert code == 1
    assert "at least 1" in captured.err


def test_fizzbuzz_command_rejects_non_integer():
    with pytest.raises(SystemExit) as exc_info:
        main(["fizzbuzz", "abc"])

    assert exc_info.value.code == 2