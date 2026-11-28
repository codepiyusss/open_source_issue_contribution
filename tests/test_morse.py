import pytest
from fixit.morse import encode, decode

def test_encode():
    assert encode("SOS") == "... --- ..."

def test_decode():
    assert decode("... --- ...") == "SOS"

def test_error():
    with pytest.raises(ValueError):
        encode("!")
