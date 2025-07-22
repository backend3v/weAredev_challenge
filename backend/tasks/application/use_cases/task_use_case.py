from tasks.domain.repositories.task_repository import TaskRepository
from tasks.domain.entities.task import Task, TaskStatus
from typing import Optional, List
from datetime import datetime

class TaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, description: str, user_id: int, due_date: Optional[datetime] = None) -> Task:
        task = Task(
            task_id=0,  # ORM will set
            description=description,
            user_id=user_id,
            status=TaskStatus.PENDING,
            due_date=due_date,
            deleted=False
        )
        return self.task_repository.create(task)

    def list_tasks_by_user(self, user_id: int) -> List[Task]:
        return self.task_repository.list_by_user(user_id)

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.task_repository.get_by_id(task_id)

    def update_task(self, task_id: int, description: Optional[str] = None, due_date: Optional[datetime] = None, status: Optional[str] = None) -> Task:
        task = self.task_repository.get_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        if description is not None:
            task.description = description
        if due_date is not None:
            task.due_date = due_date
        if status is not None:
            task.status = TaskStatus(status)
        return self.task_repository.update(task)

    def delete_task(self, task_id: int) -> None:
        self.task_repository.delete(task_id)

    def change_task_status(self, task_id: int, status: str) -> Task:
        task = self.task_repository.get_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        task.status = TaskStatus(status)
        return self.task_repository.update(task) 