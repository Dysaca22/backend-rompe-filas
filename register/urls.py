from django.urls import path
from .views import UserCreateAPIView, UserLoginView


urlpatterns = [
    path('create-user/', UserCreateAPIView.as_view(), name='create-user'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]