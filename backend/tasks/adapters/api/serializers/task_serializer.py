from rest_framework import serializers

class TaskCreateSerializer(serializers.Serializer):
    description = serializers.CharField()
    due_date = serializers.DateTimeField(required=False, allow_null=True)

class TaskUpdateSerializer(serializers.Serializer):
    description = serializers.CharField(required=False)
    due_date = serializers.DateTimeField(required=False, allow_null=True)
    status = serializers.ChoiceField(choices=["pending", "completed", "postponed"], required=False)

class TaskStatusUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=["pending", "completed", "postponed"])

class TaskResponseSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    description = serializers.CharField()
    user_id = serializers.IntegerField()
    status = serializers.CharField()
    due_date = serializers.DateTimeField(allow_null=True)
    deleted = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField() 