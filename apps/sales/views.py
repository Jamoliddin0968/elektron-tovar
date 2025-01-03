from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Sale
from .serializers import SaleCreateSerializer, SaleInfoSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().prefetch_related(
        'sale_items', "sale_items__product")
    serializer_class = SaleInfoSerializer
    permission_classes = [IsAuthenticated,]

    http_method_names = ["get", "post"]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaleCreateSerializer
        return super().get_serializer_class()
