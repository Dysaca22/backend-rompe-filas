from rest_framework import serializers

from .models import Qualify


class QualifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualify
        fields = ['rate', 'comment', 'turn']