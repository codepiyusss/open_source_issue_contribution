
import pytest

from fixit.cli import main
from fixit.config import load_config


def test_missing_config_returns_empty_dictionary(tmp_path):
    config_path = tmp_path / ".fixit.json"

    assert load_config(config_path) == {}


def test_load_config_reads_password_length(tmp_path):
    config_path = tmp_path / ".fixit.json"

    config_path.write_text(
        '{"password": {"length": 16}}',
        encoding="utf-8",
    )

    assert load_config(config_path) == {
        "password": {"length": 16}
    }


@pytest.mark.parametrize(
    "contents",
    [
        "{invalid json",
        "[]",
        '{"password": null}',
        '{"password": {"length": "16"}}',
        '{"password": {"length": 0}}',
        '{"password": {"length": true}}',
    ],
)
def test_invalid_config_is_rejected(tmp_path, contents):
    config_path = tmp_path / ".fixit.json"

    config_path.write_text(contents, encoding="utf-8")

    with pytest.raises((ValueError, TypeError), match="invalid config file"):
        load_config(config_path)


def test_password_uses_configured_length(tmp_path, capsys):
    config_path = tmp_path / ".fixit.json"

    config_path.write_text(
        '{"password": {"length": 16}}',
        encoding="utf-8",
    )

    result = main(["password"], config_path=config_path)

    generated = capsys.readouterr().out.strip()

    assert result == 0
    assert len(generated) == 16


def test_password_cli_argument_overrides_config(tmp_path, capsys):
    config_path = tmp_path / ".fixit.json"

    config_path.write_text(
        '{"password": {"length": 20}}',
        encoding="utf-8",
    )

    result = main(
        ["password", "--length", "8"],
        config_path=config_path,
    )

    generated = capsys.readouterr().out.strip()

    assert result == 0
    assert len(generated) == 8


def test_password_defaults_to_12_without_config(tmp_path, capsys):
    config_path = tmp_path / ".fixit.json"

    result = main(["password"], config_path=config_path)

    generated = capsys.readouterr().out.strip()

    assert result == 0
    assert len(generated) == 12


def test_invalid_config_returns_clear_cli_error(tmp_path, capsys):
    config_path = tmp_path / ".fixit.json"

    config_path.write_text(
        '{"password": ',
        encoding="utf-8",
    )

    result = main(["password"], config_path=config_path)

    captured = capsys.readouterr()

    assert result == 1
    assert "invalid config file" in captured.err.lower()
    assert "Traceback" not in captured.err
