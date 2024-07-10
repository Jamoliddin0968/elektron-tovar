from rest_framework import serializers

from apps.sales.serializers import SaleDebtSerializer

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerDetailSerializer(serializers.ModelSerializer):
    sales = SaleDebtSerializer(many=True)

    class Meta:
        model = Customer
        fields = '__all__'
