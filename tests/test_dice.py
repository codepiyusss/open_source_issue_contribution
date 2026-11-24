import random

import pytest

from fixit.dice import roll_dice


def test_roll_dice_is_deterministic_with_seeded_random():
    rolls, total = roll_dice("2d6", random.Random(7))

    assert rolls == [3, 2]
    assert total == 5


def test_roll_dice_accepts_uppercase_notation():
    rolls, total = roll_dice("1D2", random.Random(1))

    assert len(rolls) == 1
    assert 1 <= rolls[0] <= 2
    assert total == rolls[0]


@pytest.mark.parametrize("notation", ["0d6", "101d6", "2d1", "2d0", "2d6x", "d6", "2d"])
def test_roll_dice_rejects_invalid_notation_or_bounds(notation):
    with pytest.raises(ValueError):
        roll_dice(notation, random.Random(1))


def test_roll_dice_rejects_non_string_notation():
    with pytest.raises((TypeError, AttributeError)):
        roll_dice(None)
