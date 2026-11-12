import random
import string

def generate(length=8, use_digits=True, use_symbols=True):
    letter_pool = string.ascii_letters
    digit_pool = string.digits if use_digits else ""
    symbol_pool = string.punctuation if use_symbols else ""

    # Pick 1 guaranteed character from each active required pool
    required_chars = [random.choice(letter_pool)]
    if use_digits:
        required_chars.append(random.choice(digit_pool))
    if use_symbols:
        required_chars.append(random.choice(symbol_pool))

    # Raise ValueError if requested length is smaller than required types
    if length < len(required_chars):
        raise ValueError(
            f"Length {length} is too short for the required character types."
        )

    # Build the full pool of allowed characters
    full_pool = letter_pool + digit_pool + symbol_pool

    # Fill the remaining character slots
    remaining_slots = length - len(required_chars)
    remaining_chars = [random.choice(full_pool) for _ in range(remaining_slots)]

    # Combine and shuffle so guaranteed characters aren't always first
    all_chars = required_chars + remaining_chars
    random.shuffle(all_chars)

    return "".join(all_chars)