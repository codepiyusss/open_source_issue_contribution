import pytest
from fixit.cli import main
import json

def test_version(capsys):
    try:
        main(["--version"])
    except SystemExit:
        pass
    assert "fixit" in capsys.readouterr().out


def test_palindrome_command(capsys):
    main(["palindrome", "level"])
    assert capsys.readouterr().out.strip() == "True"


def test_wc_file_option(tmp_path, capsys):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello world\nhow are you", encoding="utf-8")

    result = main(["wc", "--file", str(file_path)])

    assert result == 0
    assert capsys.readouterr().out.strip() == "words=5 lines=2 chars=23"


def test_wc_file_not_found(capsys):
    result = main(["wc", "--file", "missing_file.txt"])

    assert result == 1
    assert "missing_file.txt" in capsys.readouterr().err

def test_wc_json_output(capsys):
    result = main(["wc", "a b", "--json"])

    captured = capsys.readouterr()
    output = json.loads(captured.out)

    assert result == 0
    assert output == {
        "words": 2,
        "lines": 1,
        "chars": 3,
    }


def test_top_words_command(capsys):
    result = main(["top-words", "Cat dog CAT bird dog.", "--n", "2"])

    assert result == 0
    assert capsys.readouterr().out == "cat: 2\ndog: 2\n"


def test_top_words_command_defaults_to_three(capsys):
    result = main(["top-words", "one two three four"])

    assert result == 0
    assert capsys.readouterr().out == "one: 1\ntwo: 1\nthree: 1\n"


def test_roman_number_to_numeral(capsys):
    result = main(["roman", "1994"])

    assert result == 0
    assert capsys.readouterr().out.strip() == "MCMXCIV"


def test_roman_numeral_to_number(capsys):
    result = main(["roman", "MCMXCIV"])

    assert result == 0
    assert capsys.readouterr().out.strip() == "1994"


def test_roman_out_of_range(capsys):
    result = main(["roman", "4000"])

    assert result == 1
    assert "between 1 and 3999" in capsys.readouterr().err


def test_roman_invalid_numeral(capsys):
    result = main(["roman", "IIII"])

    assert result == 1
    assert "not a valid Roman numeral" in capsys.readouterr().err


@pytest.mark.parametrize("value", ["nan", "inf"])
def test_convert_rejects_non_finite_values(value):
    with pytest.raises(SystemExit):
        main(["convert", value, "c2f"])