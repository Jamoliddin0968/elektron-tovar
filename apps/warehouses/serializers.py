from rest_framework import serializers

from apps.products.serializers import ProductSerializer

from .models import WareHouse


class WareHouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WareHouse
        fields = '__all__'
