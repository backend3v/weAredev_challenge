from tasks.domain.entities.user import User
from tasks.domain.repositories.user_repository import UserRepository
from typing import Optional

class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, username: str, email: str, password: str) -> User:
        # Check if user already exists
        if self.user_repository.get_by_email(email):
            raise ValueError("A user with this email already exists.")
        user = User(
            user_id=0,  # Will be set by ORM
            username=username,
            email=email,
            password_hash=password,  # Will be hashed in repository
            is_active=True,
            is_staff=False
        )
        return self.user_repository.create(user)

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        return self.user_repository.authenticate(email, password) 