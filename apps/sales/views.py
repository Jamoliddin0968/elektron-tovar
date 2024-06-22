from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Sale
from .serializers import SaleCreateSerializer, SaleInfoSerializer


@extend_schema_view(
    list=extend_schema(tags=["Sales"]),
    retrieve=extend_schema(tags=["Sales"]),
    create=extend_schema(tags=["Sales"]),
    update=extend_schema(tags=["Sales"]),
    partial_update=extend_schema(tags=["Sales"]),
    destroy=extend_schema(tags=["Sales"])
)
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleInfoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    http_method_names = ["get", "post"]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaleCreateSerializer
        return super().get_serializer_class()
