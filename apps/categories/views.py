from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category
from .serializers import CategoryProductSerializer, CategorySerializer


@extend_schema_view(
    list=extend_schema(tags=['Category']),
    retrieve=extend_schema(tags=['Category']),
    create=extend_schema(tags=['Category']),
    update=extend_schema(tags=['Category']),
    partial_update=extend_schema(tags=['Category']),
    destroy=extend_schema(tags=['Category']),
    get_by_category_id=extend_schema(tags=['Category']),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    @action(detail=False, methods=['get'], url_path='category/(?P<category_id>[^/.]+)')
    def get_by_category_id(self, request, category_id=None):
        try:
            warehouse = Category.objects.prefetch_related(
                'items').get(id=category_id)
            serializer = CategoryProductSerializer(warehouse)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Category entry not found for this product ID'}, status=404)
