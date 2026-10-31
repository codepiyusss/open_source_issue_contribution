import pytest

from fixit.jsonfmt import format_json


def test_format_json():
    assert format_json('{"a":1}') == '{\n  "a": 1\n}'


def test_invalid_json_friendly_error():
    with pytest.raises(ValueError, match="Invalid JSON"):
        format_json("{not json")
        
def test_format_json_minify():
    assert format_json('{"a": 1, "b": 2}', minify=True) == '{"a":1,"b":2}'
