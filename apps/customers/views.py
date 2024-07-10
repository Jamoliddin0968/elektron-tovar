from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerDetailSerializer, CustomerSerializer


@extend_schema_view(
    list=extend_schema(tags=["Customers"]),
    retrieve=extend_schema(tags=["Customers"]),
    create=extend_schema(tags=["Customers"]),
    update=extend_schema(tags=["Customers"]),
    partial_update=extend_schema(tags=["Customers"]),
    destroy=extend_schema(tags=["Customers"]),
    get_by_product_id=extend_schema(tags=["Customers"]),
)
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['post', 'get', 'patch']
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CustomerDetailSerializer(instance)
        return Response(serializer.data)
