"""Dice rolling helpers."""

import random
import re
from typing import List, Optional, Tuple


def roll_dice(notation: str, rng: Optional[random.Random] = None) -> Tuple[List[int], int]:
    """Roll dice described by NdM notation and return the rolls and their total."""
    match = re.fullmatch(r"(\d+)[dD](\d+)", notation.strip())
    if match is None:
        raise ValueError("dice notation must use NdM format, such as 2d6")

    count, sides = (int(value) for value in match.groups())
    if not 1 <= count <= 100:
        raise ValueError("number of dice must be between 1 and 100")
    if sides < 2:
        raise ValueError("each die must have at least 2 sides")

    generator = rng if rng is not None else random.Random()
    rolls = [generator.randint(1, sides) for _ in range(count)]
    return rolls, sum(rolls)
