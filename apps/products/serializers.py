from rest_framework.serializers import ModelSerializer

from apps.warehouses.models import WareHouse

from .models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Product

    def create(self, validated_data):
        new_product = super().create(validated_data)
        warehouse_product, _ = WareHouse.objects.get_or_create(
            product=new_product)

        return new_product
