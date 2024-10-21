from .models import Warehouse
from rest_framework import viewsets
from .serializers import WarehouseSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
