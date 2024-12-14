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


class StockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'product', 'quantity']


class StockCreateSerializer(serializers.Serializer):
    items = StockItemSerializer(many=True, write_only=True)
    price = serializers.IntegerField()

    def create(self, validated_data):
        for item in validated_data['items']:
            stock, _ = Stock.objects.get_or_create(
                product=item['product']
            )
            stock.quantity += item['quantity']
            stock.save()
        return {
            'price': validated_data['price']
        }
