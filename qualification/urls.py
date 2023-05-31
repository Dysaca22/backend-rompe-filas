from django.urls import path
from .views import QualifyView


urlpatterns = [
    path('qualify/<int:turn>/', QualifyView.as_view(), name='qualify'),
]