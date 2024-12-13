from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from apps.warehouses.filters import StockFilter

from .models import Stock, Warehouse
from .serializers import StockCreateSerializer, StockSerializer, WarehouseSerializer
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


class ReceiveCreateApiView(CreateAPIView):
    serializer_class = StockCreateSerializer
    queryset = Stock.objects.all()
