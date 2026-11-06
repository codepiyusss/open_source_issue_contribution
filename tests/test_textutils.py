import pytest

from fixit.textutils import (
    convert_case,
    is_palindrome,
    reverse_words,
    slugify,
)


def test_simple_palindrome():
    assert is_palindrome("level")


def test_palindrome_ignores_case():
    assert is_palindrome("Level")


def test_palindrome_ignores_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama")


def test_reverse_words_extra_spaces():
    assert reverse_words("hello   world") == "world hello"


def test_slugify_basic():
    assert slugify("Hello World!") == "hello-world"


def test_slugify_punctuation_and_spaces():
    assert slugify("Open Source, Project!") == "open-source-project"

def test_convert_case_snake():
    assert convert_case("snake", "Hello World") == "hello_world"


def test_convert_case_kebab():
    assert convert_case("kebab", "Hello World") == "hello-world"


def test_convert_case_camel():
    assert convert_case("camel", "Hello World") == "helloWorld"


def test_convert_case_pascal():
    assert convert_case("pascal", "Hello World") == "HelloWorld"


def test_convert_case_different_separators():
    assert (
        convert_case("pascal", "  HELLO__world--example ")
        == "HelloWorldExample"
    )


def test_convert_case_empty_text():
    assert convert_case("snake", "") == ""


def test_convert_case_invalid_style():
    with pytest.raises(ValueError, match="Unsupported style: random"):
        convert_case("random", "Hello World")
