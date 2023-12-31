from rest_framework import serializers

from .models import Transport

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'

class UpdateFreezerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ['freezer_status']

class UpdateNebulizerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ['nebulizer_status']