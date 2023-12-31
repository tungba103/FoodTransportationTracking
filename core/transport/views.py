from django.shortcuts import render

from rest_framework import viewsets, views, response

from drf_yasg.utils import swagger_auto_schema

from .serializers import Transport, TransportSerializer, UpdateFreezerStatusSerializer, UpdateNebulizerStatusSerializer

class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

class UpdateFreezerStatus(views.APIView):
    @swagger_auto_schema(
        request_body=UpdateFreezerStatusSerializer,
        responses={200: 'OK', 400: 'Bad Request'},
    )
    def patch(self, request, id):
        freezer = Transport.objects.get(id=id)
        freezer.freezer_status = request.data['freezer_status']
        freezer.save()
        return response.Response({'freezer_status': freezer.freezer_status})
    
class UpdateNebulizerStatus(views.APIView):
    @swagger_auto_schema(
        request_body=UpdateNebulizerStatusSerializer,
        responses={200: 'OK', 400: 'Bad Request'},
    )
    def patch(self, request, id):
        nebulizer = Transport.objects.get(id=id)
        nebulizer.nebulizer_status = request.data['nebulizer_status']
        nebulizer.save()
        return response.Response({'nebulizer_status': nebulizer.nebulizer_status})