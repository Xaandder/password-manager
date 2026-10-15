

import secrets
import string


def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Generate a secure password with the selected character types."""

    character_groups = []

    if use_uppercase:
        character_groups.append(string.ascii_uppercase)

    if use_lowercase:
        character_groups.append(string.ascii_lowercase)

    if use_digits:
        character_groups.append(string.digits)

    if use_symbols:
        character_groups.append("!@#$%^&*()-_=+[]{};:,.?/")

    if not character_groups:
        raise ValueError("At least one character type must be selected.")

    if length < len(character_groups):
        raise ValueError(
            "Length must be at least the number of selected character types."
        )

    characters = "".join(character_groups)

    password = [
        secrets.choice(group)
        for group in character_groups
    ]

    password.extend(
        secrets.choice(characters)
        for _ in range(length - len(password))
    )

    secrets.SystemRandom().shuffle(password)

    return "".join(password)
