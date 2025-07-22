from tasks.domain.repositories.task_repository import TaskRepository
from tasks.domain.entities.task import Task, TaskStatus
from tasks.infrastructure.models.task_model import TaskModel
from tasks.infrastructure.models.user_model import UserModel
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta

class TaskRepositoryImpl(TaskRepository):
    def get_by_id(self, task_id: int) -> Task | None:
        try:
            task_obj = TaskModel.objects.get(id=task_id, deleted=False)
            return self._to_domain(task_obj)
        except ObjectDoesNotExist:
            return None

    def list_by_user(self, user_id: int) -> list[Task]:
        tasks = TaskModel.objects.filter(user_id=user_id, deleted=False)
        return [self._to_domain(t) for t in tasks]

    def create(self, task: Task) -> Task:
        user_obj = UserModel.objects.get(id=task.user_id)
        task_obj = TaskModel.objects.create(
            description=task.description,
            user=user_obj,
            status=task.status.value,
            due_date=task.due_date,
        )
        return self._to_domain(task_obj)

    def update(self, task: Task) -> Task:
        task_obj = TaskModel.objects.get(id=task.task_id)
        task_obj.description = task.description
        task_obj.status = task.status.value
        task_obj.due_date = task.due_date
        task_obj.deleted = task.deleted
        task_obj.save()
        return self._to_domain(task_obj)

    def delete(self, task_id: int) -> None:
        task_obj = TaskModel.objects.get(id=task_id)
        task_obj.mark_deleted()

    def list_due_soon(self, user_id: int) -> list[Task]:
        now = datetime.utcnow()
        soon = now + timedelta(hours=24)
        tasks = TaskModel.objects.filter(user_id=user_id, due_date__lte=soon, due_date__gte=now, deleted=False)
        return [self._to_domain(t) for t in tasks]

    def _to_domain(self, task_obj: TaskModel) -> Task:
        return Task(
            task_id=task_obj.id,
            description=task_obj.description,
            user_id=task_obj.user_id,
            status=TaskStatus(task_obj.status),
            due_date=task_obj.due_date,
            deleted=task_obj.deleted,
            created_at=task_obj.created_at,
            updated_at=task_obj.updated_at
        ) 