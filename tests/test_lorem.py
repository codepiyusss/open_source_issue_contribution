import pytest

from fixit.cli import main
from fixit.lorem import WORDS, generate


def test_generate_five_words():
    assert generate(5) == "Lorem ipsum dolor sit amet."


def test_generate_default_is_twenty_words():
    assert generate() == generate(20)
    assert len(generate().rstrip(".").split()) == 20


def test_generate_cycles_word_list():
    count = len(WORDS) + 2
    words = generate(count).rstrip(".").split()
    assert words[len(WORDS)] == WORDS[0]
    assert words[len(WORDS) + 1] == WORDS[1]


def test_generate_one_word():
    assert generate(1) == "Lorem."


@pytest.mark.parametrize("words", [0, -3])
def test_generate_rejects_less_than_one(words):
    with pytest.raises(ValueError):
        generate(words)


def test_lorem_command(capsys):
    result = main(["lorem", "--words", "5"])

    assert result == 0
    assert capsys.readouterr().out.strip() == "Lorem ipsum dolor sit amet."


def test_lorem_command_rejects_zero_words(capsys):
    result = main(["lorem", "--words", "0"])

    assert result == 1
    assert "at least 1" in capsys.readouterr().err
