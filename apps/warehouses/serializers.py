from rest_framework import serializers

from apps.products.serializers import ProductSerializer

from .models import Stock, Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'description']


class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Stock
        fields = ['id', 'product', 'quantity']


class StockCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'product', 'quantity']

    def create(self, validated_data):
        stock, _ = Stock.objects.get_or_create(
            product=validated_data['product']
        )
        stock.quantity += validated_data['quantity']
        stock.save()
        return stock
