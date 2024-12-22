from django.db import transaction
from rest_framework import serializers

# from apps.customers.serializers import CustomerSerializer
from apps.products.serializers import ProductSerializer

from ..customers.models import Customer
from .models import Sale, SaleItem


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SaleItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        exclude = ('id', 'sale')


class SaleCreateSerializer(serializers.ModelSerializer):
    items = SaleItemCreateSerializer(many=True, write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Sale
        fields = "__all__"

    def create(self, validated_data):
        with transaction.atomic():
            items = validated_data.pop('items')
            new_sale = Sale.objects.create(**validated_data)
            new_sale_items = []
            for item in items:
                new_sale_items.append(SaleItem(**item, sale=new_sale))
            SaleItem.objects.bulk_create(new_sale_items)
            return new_sale


class SaleItemInfoSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = SaleItem
        fields = "__all__"


class SaleInfoSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer()
    items = SaleItemInfoSerializer(many=True, source="sale_items")

    class Meta:
        model = Sale
        fields = "__all__"


class SaleDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'credit', 'datetime']
