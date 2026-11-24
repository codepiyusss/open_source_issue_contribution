from datetime import date

import pytest

from fixit.dates import age_in_years


def test_age_in_completed_years():
    assert age_in_years("2000-05-17", today=date(2026, 5, 16)) == 25
    assert age_in_years("2000-05-17", today=date(2026, 5, 17)) == 26


def test_age_before_and_on_leap_day_birthday():
    assert age_in_years("2004-02-29", today=date(2024, 2, 28)) == 19
    assert age_in_years("2004-02-29", today=date(2024, 2, 29)) == 20


def test_february_29_birthday_is_observed_on_march_first_in_non_leap_year():
    assert age_in_years("2004-02-29", today=date(2025, 2, 28)) == 20
    assert age_in_years("2004-02-29", today=date(2025, 3, 1)) == 21


@pytest.mark.parametrize("birth", ["2000-2-01", "20000201", "2000-02-30", "not-a-date", ""])
def test_age_rejects_invalid_birth_dates(birth):
    with pytest.raises(ValueError):
        age_in_years(birth, today=date(2026, 1, 1))


def test_age_rejects_future_birth_date():
    with pytest.raises(ValueError, match="future"):
        age_in_years("2026-01-02", today=date(2026, 1, 1))


def test_age_defaults_to_current_date():
    expected = date.today().year - 2000
    if (date.today().month, date.today().day) < (5, 17):
        expected -= 1
    assert age_in_years("2000-05-17") == expected
