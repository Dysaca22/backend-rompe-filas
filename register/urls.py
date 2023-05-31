from django.urls import path
from .views import UserView, UserLoginView


urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]