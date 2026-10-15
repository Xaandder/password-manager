
import pytest
import string

from src.password_manager.generator import generate_password


def test_password_has_requested_length():
    password = generate_password(length=20)

    assert len(password) == 20


def test_password_uses_only_selected_characters():
    password = generate_password(
        length=100,
        use_uppercase=False,
        use_lowercase=False,
        use_digits=True,
        use_symbols=False,
    )

    assert password.isdigit()


def test_password_requires_at_least_one_character_type():
    with pytest.raises(ValueError):
        generate_password(
            use_uppercase=False,
            use_lowercase=False,
            use_digits=False,
            use_symbols=False,
        )


def test_password_rejects_invalid_length():
    with pytest.raises(ValueError):
        generate_password(length=0)

def test_password_includes_every_selected_character_type():
    password = generate_password(
        length=4,
        use_uppercase=True,
        use_lowercase=True,
        use_digits=True,
        use_symbols=True,
    )

    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.ascii_lowercase for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in "!@#$%^&*()-_=+[]{};:,.?/" for char in password)


def test_password_rejects_length_shorter_than_selected_types():
    with pytest.raises(ValueError):
        generate_password(
            length=2,
            use_uppercase=True,
            use_lowercase=True,
            use_digits=True,
            use_symbols=False,
        )
