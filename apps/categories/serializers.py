from rest_framework.serializers import ModelSerializer

from apps.products.serializers import ProductSerializer

from .models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Category


class CategoryProductSerializer(ModelSerializer):
    items = ProductSerializer(many=True)

    class Meta:
        fields = "__all__"
        model = Category
