from datetime import datetime
from typing import Optional

class User:
    """
    Domain entity representing a user. Passwords must be stored as hashes, never in plain text.
    """
    def __init__(
        self,
        user_id: int,
        username: str,
        email: str,
        password_hash: str,
        is_active: bool = True,
        is_staff: bool = False,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash  # Store only hashed passwords
        self.is_active = is_active
        self.is_staff = is_staff
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def check_password(self, raw_password: str) -> bool:
        """
        Checks if the provided password matches the stored hash.
        The actual implementation should use a secure hash function (e.g., PBKDF2, bcrypt).
        """
        raise NotImplementedError("Password checking must be implemented in the infrastructure layer.") 