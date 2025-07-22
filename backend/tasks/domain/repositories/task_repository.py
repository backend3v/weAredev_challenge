from abc import ABC, abstractmethod
from typing import List, Optional
from tasks.domain.entities.task import Task

class TaskRepository(ABC):
    """
    Abstract repository interface for Task entity.
    """
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def list_by_user(self, user_id: int) -> List[Task]:
        pass

    @abstractmethod
    def create(self, task: Task) -> Task:
        pass

    @abstractmethod
    def update(self, task: Task) -> Task:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> None:
        pass

    @abstractmethod
    def list_due_soon(self, user_id: int) -> List[Task]:
        """
        List tasks for a user that are due soon (e.g., next 24h).
        """
        pass 