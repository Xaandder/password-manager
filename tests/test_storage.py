
import json

import pytest
from cryptography.fernet import Fernet

from src.password_manager.storage import PasswordStorage


@pytest.fixture
def storage(tmp_path):
    key = Fernet.generate_key()
    file_path = tmp_path / "passwords.json"
    return PasswordStorage(str(file_path), key)


def test_password_is_saved_encrypted(storage):
    storage.add_password(
        "GitHub",
        "usuario123",
        "MiClaveSegura123!",
    )

    data = json.loads(storage.file_path.read_text(encoding="utf-8"))

    assert data["GitHub"]["username"] == "usuario123"
    assert data["GitHub"]["password"] != "MiClaveSegura123!"
    assert "MiClaveSegura123!" not in storage.file_path.read_text(
        encoding="utf-8"
    )


def test_password_can_be_retrieved(storage):
    storage.add_password("GitHub", "usuario123", "Clave123!")

    result = storage.get_password("GitHub")

    assert result == {
        "service": "GitHub",
        "username": "usuario123",
        "password": "Clave123!",
    }


def test_password_can_be_deleted(storage):
    storage.add_password("GitHub", "usuario123", "Clave123!")

    storage.delete_password("GitHub")

    with pytest.raises(KeyError):
        storage.get_password("GitHub")


def test_missing_service_raises_error(storage):
    with pytest.raises(KeyError):
        storage.get_password("ServicioInexistente")


def test_empty_password_is_rejected(storage):
    with pytest.raises(ValueError):
        storage.add_password("GitHub", "usuario123", "")


def test_empty_service_is_rejected(storage):
    with pytest.raises(ValueError):
        storage.add_password("", "usuario123", "Clave123!")


def test_wrong_key_cannot_decrypt_password(tmp_path):
    file_path = tmp_path / "passwords.json"

    storage1 = PasswordStorage(str(file_path), Fernet.generate_key())
    storage1.add_password("GitHub", "usuario123", "Clave123!")

    storage2 = PasswordStorage(str(file_path), Fernet.generate_key())

    with pytest.raises(ValueError, match="Could not decrypt"):
        storage2.get_password("GitHub")
