
"""Load user-level defaults from a JSON configuration file."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_config(config_path: Path | None = None) -> dict[str, Any]:
    """Load configuration from a JSON file.

    A missing file means that no custom defaults are configured."""
    path = (Path(config_path)
            if config_path is not None
            else Path.home() / ".fixit.json"
    )

    try:
        raw_config = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}
    except UnicodeDecodeError as exc:
        raise ValueError(
            f"Error: config file '{path}' is not valid UTF-8"
        ) from exc
    except OSError as exc:
        raise ValueError(
            f"Error: cannot read config file '{path}': {exc}"
        ) from exc

    try:
        config = json.loads(raw_config)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Error: invalid config file '{path}' "
            f"at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc

    if not isinstance(config, dict):
        raise TypeError(
            f"Error: invalid config file '{path}': ""expected a JSON object"
        )

    password_config = config.get("password", {})

    if not isinstance(password_config, dict):
        raise TypeError(
            f"Error: invalid config file '{path}': ""'password' must be a JSON object"
        )

    if "length" in password_config:
        length = password_config["length"]

        if isinstance(length, bool) or not isinstance(length, int):
            raise TypeError(
                f"Error: invalid config file '{path}': "
                "'password.length' must be an integer"
            )

        if length <= 0:
            raise ValueError(
                f"Error: invalid config file '{path}': "
                "'password.length' must be a positive integer"
            )

    return config
