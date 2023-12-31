from rest_framework import serializers

from .models import Humidity

class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = ('id', 'value', 'timestamp')