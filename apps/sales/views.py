from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        out_serializer = SaleInfoSerializer(serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(out_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
