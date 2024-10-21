from django.urls import include, path
from rest_framework import routers

from .views import WarehouseViewSet

router = routers.DefaultRouter()


router.register(r'warehouses', WarehouseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
