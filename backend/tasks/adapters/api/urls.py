from django.urls import path
from tasks.adapters.api.views.user_view import UserRegisterView, UserLoginView, UserListView
from tasks.adapters.api.views.task_view import TaskListCreateView, TaskDetailView, TaskStatusUpdateView

urlpatterns = [
    # User endpoints
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('users/', UserListView.as_view(), name='user-list'),

    # Task endpoints
    path('tasks/<int:user_id>/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/detail/<int:task_id>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/status/<int:task_id>/', TaskStatusUpdateView.as_view(), name='task-status-update'),
] 