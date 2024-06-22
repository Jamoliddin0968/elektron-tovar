from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from .models import Product
# from .models import Product, ProductImage
from .serializers import ProductSerializer


@extend_schema_view(
    list=extend_schema(tags=["Products"]),
    retrieve=extend_schema(tags=["Products"]),
    create=extend_schema(tags=["Products"]),
    update=extend_schema(tags=["Products"]),
    partial_update=extend_schema(tags=["Products"]),
    destroy=extend_schema(tags=["Products"]),
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
