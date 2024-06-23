from rest_framework import serializers

from apps.products.serializers import ProductSerializer

from .models import WareHouseItem


class WareHouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WareHouseItem
        fields = '__all__'
