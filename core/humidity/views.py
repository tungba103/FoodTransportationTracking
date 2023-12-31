from django.shortcuts import render

from rest_framework import viewsets, views, response
from rest_framework import permissions, authentication

from .serializers import Humidity
from .serializers import HumiditySerializer

class HumidityViewSet(viewsets.ModelViewSet):
    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer
    # authentication_classes = (authentication.BasicAuthentication, authentication.SessionAuthentication)
    # permission_classes = (permissions.IsAuthenticated,)

class CurrentHumidity(views.APIView):
    # authentication_classes = (authentication.BasicAuthentication, authentication.SessionAuthentication)
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):
        humidity = Humidity.objects.latest('id')
        serializer = HumiditySerializer(humidity)
        return response.Response(serializer.data)