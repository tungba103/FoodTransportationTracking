from django.shortcuts import render

from rest_framework import viewsets, views, response


from .serializers import Temperature
from .serializers import TemperatureSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import Http404

class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class getListTemperatureByTransport(views.APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('start_date', openapi.IN_QUERY, description='Start date for temperature data', type=openapi.TYPE_STRING),
            openapi.Parameter('end_date', openapi.IN_QUERY, description='End date for temperature data', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, format=None):
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        if not start_date or not end_date:
            raise Http404("Both start_date and end_date query parameters are required.")

        try:
            temperatures = Temperature.objects.filter(
                timestamp__gte=start_date,
                timestamp__lte=end_date
            )
            serializer = TemperatureSerializer(temperatures, many=True)
            return response.Response(serializer.data)
        except Temperature.DoesNotExist:
            raise Http404("No temperature data found in the specified date range.")

class CurrentTemperature(views.APIView):
    def get(self, request, format=None):
        temperature = Temperature.objects.latest('id')
        serializer = TemperatureSerializer(temperature)
        return response.Response(serializer.data)