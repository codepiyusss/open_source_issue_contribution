"""Hash text with common algorithms."""

import hashlib

SUPPORTED_ALGORITHMS = ("md5", "sha1", "sha256")


def hash_text(text: str, algo: str = "sha256") -> str:
    """Return the hex digest of ``text`` encoded as UTF-8.

    Raises ValueError if ``algo`` is not one of SUPPORTED_ALGORITHMS.
    """
    if algo not in SUPPORTED_ALGORITHMS:
        raise ValueError(f"Error: unsupported algorithm '{algo}'")
    return hashlib.new(algo, text.encode("utf-8")).hexdigest()
