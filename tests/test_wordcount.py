import pytest

from fixit.wordcount import count_chars, count_lines, count_words, top_words


def test_count_words_simple():
    assert count_words("hello world") == 2


def test_count_words_extra_spaces():
    assert count_words("hello    world") == 2


def test_count_words_empty():
    assert count_words("") == 0


def test_count_lines_trailing_newline():
    assert count_lines("a\nb\n") == 2


def test_count_lines_empty():
    assert count_lines("") == 0


def test_count_words_whitespace_only():
    assert count_words(" \t\n ") == 0


def test_count_chars():
    assert count_chars("abc") == 3


def test_top_words_ignores_case_and_punctuation():
    assert top_words("Cat, dog! CAT; bird dog.", 2) == [("cat", 2), ("dog", 2)]


def test_top_words_preserves_first_seen_order_for_ties():
    assert top_words("pear apple pear apple") == [("pear", 2), ("apple", 2)]


def test_top_words_empty_text():
    assert top_words("") == []


def test_top_words_requires_positive_n():
    with pytest.raises(ValueError, match="at least 1"):
        top_words("hello", 0)
