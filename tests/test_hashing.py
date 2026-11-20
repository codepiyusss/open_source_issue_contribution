import hashlib

import pytest

from fixit.cli import main
from fixit.hashing import hash_text


def test_md5_of_hello():
    assert hash_text("hello", "md5") == "5d41402abc4b2a76b9719d911017c592"


def test_sha256_is_default():
    assert hash_text("hello") == hashlib.sha256(b"hello").hexdigest()


def test_empty_text_hashes_to_known_md5():
    assert hash_text("", "md5") == "d41d8cd98f00b204e9800998ecf8427e"


def test_unsupported_algorithm_raises():
    with pytest.raises(ValueError):
        hash_text("hello", "sha512")


def test_hash_command_default_sha256(capsys):
    assert main(["hash", "hello"]) == 0
    assert capsys.readouterr().out.strip() == hashlib.sha256(b"hello").hexdigest()


def test_hash_command_md5(capsys):
    assert main(["hash", "hello", "--algo", "md5"]) == 0
    assert capsys.readouterr().out.strip() == "5d41402abc4b2a76b9719d911017c592"


def test_hash_command_rejects_unknown_algo(capsys):
    with pytest.raises(SystemExit):
        main(["hash", "hello", "--algo", "sha512"])
