
import json
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken


class PasswordStorage:
    """Store account credentials encrypted in a JSON file."""

    def __init__(self, file_path: str, key: bytes):
        self.file_path = Path(file_path)
        self.cipher = Fernet(key)

    def _load_data(self) -> dict:
        if not self.file_path.exists():
            return {}

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Invalid storage file format.")

        return data

    def _save_data(self, data: dict) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def add_password(
        self,
        service: str,
        username: str,
        password: str,
    ) -> None:
        if not service.strip() or not username.strip():
            raise ValueError("Service and username cannot be empty.")

        if not password:
            raise ValueError("Password cannot be empty.")

        data = self._load_data()
        encrypted_password = self.cipher.encrypt(
            password.encode("utf-8")
        ).decode("utf-8")

        data[service] = {
            "username": username,
            "password": encrypted_password,
        }

        self._save_data(data)

    def get_password(self, service: str) -> dict:
        data = self._load_data()

        if service not in data:
            raise KeyError(f"Service not found: {service}")

        record = data[service]

        try:
            password = self.cipher.decrypt(
                record["password"].encode("utf-8")
            ).decode("utf-8")
        except (InvalidToken, KeyError, TypeError, UnicodeDecodeError) as exc:
            raise ValueError(
                "Could not decrypt the stored password."
            ) from exc

        return {
            "service": service,
            "username": record["username"],
            "password": password,
        }

    def delete_password(self, service: str) -> None:
        data = self._load_data()

        if service not in data:
            raise KeyError(f"Service not found: {service}")

        del data[service]
        self._save_data(data)
