from rest_framework import serializers

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UserResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    is_active = serializers.BooleanField()
    is_staff = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField() 