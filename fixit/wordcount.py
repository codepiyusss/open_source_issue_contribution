"""Word, line and character counting."""

from __future__ import annotations

import re
from collections import Counter
import json

def count_words(text: str) -> int:
    """Count the words in the given text.

    Example:
        count_words("hello world") returns 2.
        count_words("one two three") returns 3.
    """
    return len(text.split())


def count_lines(text: str) -> int:
    """Count the lines in the given text.

    Example:
        count_lines("hello\nworld") returns 2.
        count_lines("hello") returns 1.
    """
    return len(text.splitlines())


def count_chars(text: str) -> int:
    """Count the characters in the given text.

    Example:
        count_chars("hello") returns 5.
        count_chars("hi!") returns 3.
    """
    return len(text)

def prepare_json(text: str) -> str:
    """Prepare a JSON string from the given text.

    Example:
        prepare_json("a b") returns '{"words": 2, "lines": 1, "chars": 3}'.
    """
    wcjson = {}
    wcjson["words"] = count_words(text)
    wcjson["lines"] = count_lines(text)
    wcjson["chars"] = count_chars(text)
    return json.dumps(wcjson)

def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """Return up to n most frequent words and their counts.

    Words are matched case-insensitively; punctuation is treated as a
    separator. Ties retain the order in which words first appeared.
    """
    if n < 1:
        raise ValueError("n must be at least 1")

    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words).most_common(n)
