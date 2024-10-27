from rest_framework import serializers

from apps.products.serializers import ProductSerializer

from .models import Stock, Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'description']


class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    # warehouse = WarehouseSerializer()

    class Meta:
        model = Stock
        fields = ['id', 'product', 'warehouse', 'quantity']
