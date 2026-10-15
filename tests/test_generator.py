
import pytest

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
