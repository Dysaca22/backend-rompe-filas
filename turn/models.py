from django.db import models
from django.contrib.auth.models import User


class Turn(models.Model):
    TIME_OPTIONS = {
        ('08:00 - 10:00', '08:00 - 10:00'),
        ('10:00 - 12:00', '10:00 - 12:00'),
        ('12:00 - 14:00', '12:00 - 14:00'),
        ('14:00 - 16:00', '14:00 - 16:00'),
        ('16:00 - 18:00', '16:00 - 18:00'),
        ('18:00 - 20:00', '18:00 - 20:00'),
    }

    date = models.DateField()
    time = models.CharField(choices=TIME_OPTIONS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)