from django.urls import include, path
from rest_framework import routers

from .views import ReceiveCreateApiView, StockViewSet, WarehouseViewSet

router = routers.DefaultRouter()


router.register(r'warehouses', WarehouseViewSet)
router.register(r'stocks', StockViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('receive/', ReceiveCreateApiView.as_view()),
]
