from rest_framework import serializers

# from apps.customers.serializers import CustomerSerializer
from apps.products.serializers import ProductSerializer

from .models import Sale, SaleItem
from ..customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SaleItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = "__all__"


class SaleCreateSerializer(serializers.ModelSerializer):
    items = SaleItemCreateSerializer(many=True, source="sale_items")
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Sale
        fields = "__all__"

    def create(self, validated_data):
        items = validated_data.pop('items')
        new_sale = Sale.objects.create(**validated_data)
        new_sale_items = []
        for item in items:
            new_sale_items.append(SaleItem(**item))
        SaleItem.objects.bulk_create(new_sale_items)
        if new_sale.credit > 0:
            new_sale.customer.credit += new_sale.credit
            new_sale.save()
        return new_sale


class SaleItemInfoSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = SaleItem
        fields = "__all__"


class SaleInfoSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    items = SaleItemInfoSerializer(many=True, source="sale_items")

    class Meta:
        model = Sale
        fields = "__all__"


class SaleDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'credit', 'datetime']
