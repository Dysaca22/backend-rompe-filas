from django.urls import path
from .views import ListQualifyView, QualifyView


urlpatterns = [
    path('list-qualify/', ListQualifyView.as_view(), name='list-qualify'),
    path('qualify/<int:turn>/', QualifyView.as_view(), name='qualify'),
]