from django.urls import path
from .views import UserTurn


urlpatterns = [
    path('turn/', UserTurn.as_view(), name='turn'),
]