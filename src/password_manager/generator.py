
import secrets
import string


def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Generate a secure random password with the selected character types."""
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{};:,.?/"

    if not characters:
        raise ValueError("At least one character type must be selected.")

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )
