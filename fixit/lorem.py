"""Placeholder lorem ipsum text generation."""

WORDS = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing",
    "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore",
    "et", "dolore", "magna", "aliqua", "enim", "ad", "minim", "veniam",
    "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "aliquip",
]


def generate(words: int = 20) -> str:
    """Return a lorem ipsum sentence made of the given number of words.

    The word list is cycled, so the same count always gives the same text.
    The first word is capitalized and the sentence ends with a period.

    >>> generate(5)
    'Lorem ipsum dolor sit amet.'
    """
    if isinstance(words, bool) or not isinstance(words, int) or words < 1:
        raise ValueError("words must be at least 1")
    picked = [WORDS[i % len(WORDS)] for i in range(words)]
    picked[0] = picked[0].capitalize()
    return " ".join(picked) + "."
