from django.shortcuts import render

from rest_framework import viewsets, views, response
from rest_framework import permissions, authentication

from .serializers import Humidity
from .serializers import HumiditySerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import Http404

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
    
class getListHumidityByTransport(views.APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('start_date', openapi.IN_QUERY, description='Start date for Humidity data', type=openapi.TYPE_STRING),
            openapi.Parameter('end_date', openapi.IN_QUERY, description='End date for Humidity data', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, format=None):
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        if not start_date or not end_date:
            raise Http404("Both start_date and end_date query parameters are required.")

        try:
            humidities = Humidity.objects.filter(
                timestamp__gte=start_date,
                timestamp__lte=end_date
            )
            serializer = HumiditySerializer(humidities, many=True)
            return response.Response(serializer.data)
        except Humidity.DoesNotExist:
            raise Http404("No humidity data found in the specified date range.")
