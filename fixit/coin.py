"""Coin flip simulation."""

from __future__ import annotations

import random

SIDES = ("Heads", "Tails")


def flip(count: int = 1, rng: random.Random | None = None) -> list[str]:
    """Flip a coin count times and return the results as a list.

    Pass a seeded random.Random as rng to make results repeatable in tests.
    """
    if count <= 0:
        raise ValueError("count must be at least 1")
    if rng is None:
        rng = random.Random()
    return [rng.choice(SIDES) for _ in range(count)]
