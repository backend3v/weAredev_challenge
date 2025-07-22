from datetime import datetime
from enum import Enum
from typing import Optional

class TaskStatus(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    POSTPONED = 'postponed'

class Task:
    """
    Domain entity representing a task assigned to a user.
    """
    def __init__(
        self,
        task_id: int,
        description: str,
        user_id: int,
        status: TaskStatus = TaskStatus.PENDING,
        due_date: Optional[datetime] = None,
        deleted: bool = False,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.task_id = task_id
        self.description = description
        self.user_id = user_id
        self.status = status
        self.due_date = due_date
        self.deleted = deleted
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def mark_completed(self):
        """
        Mark the task as completed.
        """
        self.status = TaskStatus.COMPLETED
        self.updated_at = datetime.utcnow()

    def mark_postponed(self):
        """
        Mark the task as postponed.
        """
        self.status = TaskStatus.POSTPONED
        self.updated_at = datetime.utcnow()

    def mark_deleted(self):
        """
        Logically delete the task (soft delete).
        """
        self.deleted = True
        self.updated_at = datetime.utcnow() 