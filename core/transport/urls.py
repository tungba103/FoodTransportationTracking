from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import TransportViewSet, UpdateFreezerStatus, UpdateNebulizerStatus

# router = DefaultRouter()
# router.register('transport', TransportViewSet)
# urlpatterns = router.urls

urlpatterns = [
  path('transport', TransportViewSet.as_view({'get': 'list', 'post': 'create'})),
  path('transport/<int:pk>', TransportViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),
  path('transport/update-freezer/<int:id>', UpdateFreezerStatus.as_view()),
  path('transport/update-nebulizer/<int:id>', UpdateNebulizerStatus.as_view()),
]