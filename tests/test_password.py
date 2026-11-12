import pytest
import string
from fixit.password import generate

def test_password_guarantees_all_selected_types():
    # Loop 500 times to verify consistency across random outputs
    for _ in range(500):
        pwd = generate(length=8, use_digits=True, use_symbols=True)

        assert len(pwd) == 8
        assert any(c in string.ascii_letters for c in pwd), f"Password '{pwd}' missing letter"
        assert any(c in string.digits for c in pwd), f"Password '{pwd}' missing digit"
        assert any(c in string.punctuation for c in pwd), f"Password '{pwd}' missing symbol"

def test_password_length_too_short_raises_value_error():
    # 3 required types (letters, digits, symbols) -> minimum length is 3
    with pytest.raises(ValueError):
        generate(length=2, use_digits=True, use_symbols=True)

    # 2 required types (letters, digits) -> minimum length is 2
    with pytest.raises(ValueError):
        generate(length=1, use_digits=True, use_symbols=False)