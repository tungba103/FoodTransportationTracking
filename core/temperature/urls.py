# from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import TemperatureViewSet, CurrentTemperature, getListTemperatureByTransport

# router = DefaultRouter()
# router.register('temperature', TemperatureViewSet)
# urlpatterns = router.urls

# from .views import TemperatureListView

urlpatterns = [
    path('tensor-temperature', TemperatureViewSet.as_view({'get': 'list'}), name='temperature-list'),
    path('transport/current-temperature', CurrentTemperature.as_view(), name='current-temperature'),
    path('transport/list-temperature', getListTemperatureByTransport.as_view(), name='list-temperature'),
]