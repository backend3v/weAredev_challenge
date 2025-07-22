from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.adapters.api.serializers.user_serializer import (
    UserRegisterSerializer, UserLoginSerializer, UserResponseSerializer
)
from tasks.application.use_cases.user_use_case import UserUseCase
from tasks.infrastructure.repository_impl.user_repository_impl import UserRepositoryImpl

class UserRegisterView(APIView):
    """
    Endpoint for user registration.
    """
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            use_case = UserUseCase(UserRepositoryImpl())
            try:
                user = use_case.register_user(
                    username=serializer.validated_data['username'],
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password']
                )
                response_serializer = UserResponseSerializer(user.__dict__)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    """
    Endpoint for user login/authentication.
    """
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            use_case = UserUseCase(UserRepositoryImpl())
            user = use_case.authenticate_user(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            if user:
                response_serializer = UserResponseSerializer(user.__dict__)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 