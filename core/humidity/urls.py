# from rest_framework.routers import DefaultRouter

from .views import HumidityViewSet, CurrentHumidity
from django.urls import path

# router = DefaultRouter()
# router.register('humidity', HumidityViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('tensor-humidity', HumidityViewSet.as_view({'get': 'list'}), name='humidity-list'),
    path('transport/current-humidity', CurrentHumidity.as_view(), name='current-humidity'),
]