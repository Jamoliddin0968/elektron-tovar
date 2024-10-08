from drf_spectacular.openapi import OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import WareHouseItem
from .serializers import WareHouseSerializer


@extend_schema_view(
    list=extend_schema(tags=["Warehouse"]),
    retrieve=extend_schema(tags=["Warehouse"]),
    create=extend_schema(tags=["Warehouse"]),
    update=extend_schema(tags=["Warehouse"]),
    partial_update=extend_schema(tags=["Warehouse"]),
    destroy=extend_schema(tags=["Warehouse"]),
    get_by_product_id=extend_schema(tags=["Warehouse"]),
)
class WareHouseViewSet(viewsets.ModelViewSet):
    queryset = WareHouseItem.objects.all()
    serializer_class = WareHouseSerializer

    http_method_names = ["get",]

    @action(detail=False, methods=['get'], url_path='product/(?P<product_id>[^/.]+)')
    def get_by_product_id(self, request, product_id=None):
        try:
            warehouse = WareHouseItem.objects.get(product__id=product_id)
            serializer = WareHouseSerializer(warehouse)
            return Response(serializer.data)
        except WareHouseItem.DoesNotExist:
            return Response({'error': 'Warehouse entry not found for this product ID'}, status=404)
