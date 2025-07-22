from django.urls import path
from tasks.adapters.api.views.user_view import UserRegisterView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
] 