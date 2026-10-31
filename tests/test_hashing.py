
import pytest

from fixit.hashing import hash_text


def test_hash_md5():
    assert hash_text("hello", "md5") == "5d41402abc4b2a76b9719d911017c592"


def test_hash_sha1():
    assert hash_text("hello", "sha1") == "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"


def test_hash_sha256_default():
    assert hash_text("hello") == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"


def test_hash_empty_string():
    assert hash_text("") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def test_hash_invalid_algorithm():
    with pytest.raises(ValueError, match="Unsupported algorithm"):
        hash_text("hello", "invalid")
