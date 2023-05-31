from django.db import models
from django.contrib.auth.models import User


class Turn(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)