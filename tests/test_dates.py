from datetime import date

import pytest

from fixit.cli import main
from fixit.dates import days_until


def test_days_until_future_date():
    assert days_until("2026-12-25", today=date(2026, 12, 20)) == 5


def test_days_until_same_day():
    assert days_until("2026-12-25", today=date(2026, 12, 25)) == 0


def test_days_until_past_date():
    assert days_until("2026-12-10", today=date(2026, 12, 20)) == -10


def test_days_until_invalid_date():
    with pytest.raises(ValueError):
        days_until("2026-02-30", today=date(2026, 1, 1))

    with pytest.raises(ValueError):
        days_until("25-12-2026", today=date(2026, 1, 1))


def test_cli_days_until_past_date(capsys):
    exit_code = main(["days-until", "2020-01-01"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "This date has already passed."
