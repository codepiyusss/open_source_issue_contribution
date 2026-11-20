import pytest

from fixit import bases
from fixit.cli import main


def test_to_bases_example():
    assert bases.to_bases(255) == "0b11111111 0o377 0xff"


def test_to_bases_zero():
    assert bases.to_bases(0) == "0b0 0o0 0x0"


def test_to_bases_negative_raises():
    with pytest.raises(ValueError):
        bases.to_bases(-1)


def test_base_command(capsys):
    result = main(["base", "255"])

    assert result == 0
    assert capsys.readouterr().out.strip() == "0b11111111 0o377 0xff"


def test_base_command_rejects_negative(capsys):
    result = main(["base", "-5"])

    assert result == 1
    assert "non-negative" in capsys.readouterr().err
