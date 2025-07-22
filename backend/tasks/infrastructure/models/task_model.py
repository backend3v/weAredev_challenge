from django.db import models
from tasks.infrastructure.models.user_model import UserModel
from enum import Enum

class TaskStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    COMPLETED = 'completed', 'Completed'
    POSTPONED = 'postponed', 'Postponed'

class TaskModel(models.Model):
    description = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.PENDING)
    due_date = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_completed(self):
        self.status = TaskStatus.COMPLETED
        self.save()

    def mark_postponed(self):
        self.status = TaskStatus.POSTPONED
        self.save()

    def mark_deleted(self):
        self.deleted = True
        self.save()

    def __str__(self):
        return f"Task({self.id}): {self.description[:20]}..." 