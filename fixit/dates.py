from datetime import date
from typing import Optional, Union


def days_until(target_date: str, today: Optional[Union[date, str]] = None) -> int:
    """Return the number of days from today until target_date (YYYY-MM-DD).
    Returns a negative integer if target_date is in the past.
    Raises ValueError if target_date (or today, if given as a string) is invalid.
    """
    target = date.fromisoformat(target_date)

    if today is None:
        base = date.today()
    elif isinstance(today, str):
        base = date.fromisoformat(today)
    else:
        base = today

    return (target - base).days
