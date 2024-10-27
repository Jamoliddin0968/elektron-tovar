from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.warehouses.filters import StockFilter

from .models import Stock, Warehouse
from .serializers import StockSerializer, WarehouseSerializer
from django_filters.rest_framework import DjangoFilterBackend


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = StockFilter

    def get_queryset(self):
        warehouse = self.request.user.warehouse
        qs = super().get_queryset()
        return qs.filter(warehouse=warehouse)
