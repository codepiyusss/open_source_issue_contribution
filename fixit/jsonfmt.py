"""JSON pretty-printer."""

import json


def format_json(raw: str, indent: int = 2, minify: bool = False) -> str:
    """Format a JSON string with indentation or minify it.

    Example:
        format_json('{"name":"Sam"}') returns '{\n  "name": "Sam"\n}'.
    """
    try:
        data = json.loads(raw)
        if minify:
            return json.dumps(data, separators=(",", ":"))
        return json.dumps(data, indent=indent)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON")
