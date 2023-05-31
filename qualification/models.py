from django.db import models
from turn.models import Turn


class Qualify(models.Model):
    RATES_OPTIONS = {
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    }

    rate = models.IntegerField(choices=RATES_OPTIONS)
    comment = models.CharField(max_length=500, blank=True)
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE)