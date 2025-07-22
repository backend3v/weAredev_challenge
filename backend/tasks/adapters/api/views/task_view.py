from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.adapters.api.serializers.task_serializer import (
    TaskCreateSerializer, TaskUpdateSerializer, TaskResponseSerializer, TaskStatusUpdateSerializer
)
from tasks.application.use_cases.task_use_case import TaskUseCase
from tasks.infrastructure.repository_impl.task_repository_impl import TaskRepositoryImpl

class TaskListCreateView(APIView):
    """
    GET: List all tasks for a user.
    POST: Create a new task.
    """
    def get(self, request, user_id):
        use_case = TaskUseCase(TaskRepositoryImpl())
        tasks = use_case.list_tasks_by_user(user_id)
        serializer = TaskResponseSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            use_case = TaskUseCase(TaskRepositoryImpl())
            task = use_case.create_task(
                description=serializer.validated_data['description'],
                user_id=user_id,
                due_date=serializer.validated_data.get('due_date')
            )
            response_serializer = TaskResponseSerializer(task.__dict__)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    """
    GET: Retrieve a task.
    PUT: Update a task.
    DELETE: Logically delete a task.
    """
    def get(self, request, task_id):
        use_case = TaskUseCase(TaskRepositoryImpl())
        task = use_case.get_task(task_id)
        if not task:
            return Response({'detail': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskResponseSerializer(task.__dict__)
        return Response(serializer.data)

    def put(self, request, task_id):
        serializer = TaskUpdateSerializer(data=request.data)
        if serializer.is_valid():
            use_case = TaskUseCase(TaskRepositoryImpl())
            task = use_case.update_task(
                task_id=task_id,
                description=serializer.validated_data.get('description'),
                due_date=serializer.validated_data.get('due_date'),
                status=serializer.validated_data.get('status')
            )
            response_serializer = TaskResponseSerializer(task.__dict__)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        use_case = TaskUseCase(TaskRepositoryImpl())
        use_case.delete_task(task_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskStatusUpdateView(APIView):
    """
    PATCH: Change the status of a task.
    """
    def patch(self, request, task_id):
        serializer = TaskStatusUpdateSerializer(data=request.data)
        if serializer.is_valid():
            use_case = TaskUseCase(TaskRepositoryImpl())
            task = use_case.change_task_status(
                task_id=task_id,
                status=serializer.validated_data['status']
            )
            response_serializer = TaskResponseSerializer(task.__dict__)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 