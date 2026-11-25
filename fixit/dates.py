"""Date-related calculations."""

import re
from datetime import date
from typing import Optional, Union


def age_in_years(birth: str, today: Optional[date] = None) -> int:
    """Return completed years between a birth date and today.

    A 29 February birthday is observed on 1 March in non-leap years.
    """
    if not isinstance(birth, str) or re.fullmatch(r"\d{4}-\d{2}-\d{2}", birth) is None:
        raise ValueError("birth date must use YYYY-MM-DD format")

    try:
        birth_date = date.fromisoformat(birth)
    except ValueError as exc:
        raise ValueError("birth date must be a valid YYYY-MM-DD date") from exc

    current_date = date.today() if today is None else today
    if not isinstance(current_date, date):
        raise ValueError("today must be a date")

    if birth_date > current_date:
        raise ValueError("birth date cannot be in the future")

    anniversary_day = birth_date.day
    anniversary_month = birth_date.month
    if birth_date.month == 2 and birth_date.day == 29:
        if not _is_leap_year(current_date.year):
            anniversary_month = 3
            anniversary_day = 1

    age = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (anniversary_month, anniversary_day):
        age -= 1
    return age


def _is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



def days_until(target_date: str, today: Optional[Union[date, str]] = None) -> int:
    """Return the number of days from today until target_date (YYYY-MM-DD)."""
    target = date.fromisoformat(target_date)
    if today is None:
        base = date.today()
    elif isinstance(today, str):
        base = date.fromisoformat(today)
    else:
        base = today
    return (target - base).days
