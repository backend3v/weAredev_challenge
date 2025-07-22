from abc import ABC, abstractmethod
from typing import Optional
from tasks.domain.entities.user import User

class UserRepository(ABC):
    """
    Abstract repository interface for User entity.
    """
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass

    @abstractmethod
    def authenticate(self, email: str, password: str) -> Optional[User]:
        """
        Validate user credentials. Should return the user if valid, None otherwise.
        """
        pass 