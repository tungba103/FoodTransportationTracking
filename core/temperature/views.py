from django.shortcuts import render

from rest_framework import viewsets, views, response


from .serializers import Temperature
from .serializers import TemperatureSerializer

class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class CurrentTemperature(views.APIView):
    def get(self, request, format=None):
        temperature = Temperature.objects.latest('id')
        serializer = TemperatureSerializer(temperature)
        return response.Response(serializer.data)