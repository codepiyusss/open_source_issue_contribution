import pytest

from fixit.jsonfmt import format_json


def test_format_json():
    assert format_json('{"a":1}') == '{\n  "a": 1\n}'


def test_invalid_json_friendly_error():
    with pytest.raises(ValueError, match="Invalid JSON"):
        format_json("{not json")


def test_format_json_custom_indent():
    assert format_json('{"a":1}', indent=4) == '{\n    "a": 1\n}'


def test_format_json_nested_objects():
    assert format_json('{"a":{"b":1}}') == '{\n  "a": {\n    "b": 1\n  }\n}'


def test_format_json_list():
    assert format_json('{"items":[1,2]}') == '{\n  "items": [\n    1,\n    2\n  ]\n}'


def test_format_json_empty_object():
    assert format_json('{}') == '{}'


def test_format_json_numbers():
    assert format_json('{"a":10,"b":2.5}') == '{\n  "a": 10,\n  "b": 2.5\n}'
