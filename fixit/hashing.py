
"""Hashing utilities."""

import hashlib


def hash_text(text: str, algo: str = "sha256") -> str:
    """Return the hexadecimal hash digest of the given text."""
    supported_algorithms = ("md5", "sha1", "sha256")

    if algo not in supported_algorithms:
        raise ValueError(f"Unsupported algorithm: {algo}")

    hash_object = hashlib.new(algo)
    hash_object.update(text.encode("utf-8"))
    return hash_object.hexdigest()
