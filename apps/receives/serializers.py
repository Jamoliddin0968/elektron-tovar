from rest_framework import serializers

from apps.products.models import Product
from apps.warehouses.models import Stock

from .models import Receive, ReceiveItem


class ReceiveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiveItem
        exclude = ('receive',)


class ReceiveSerializer(serializers.ModelSerializer):
    items = ReceiveItemSerializer(many=True, write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Receive
        fields = "__all__"

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        receive = Receive.objects.create(**validated_data)
        for item_data in items_data:
            new_receive_item = ReceiveItem.objects.create(
                receive=receive, **item_data)

            obj, _ = Stock.objects.get_or_create(
                product=new_receive_item.product
            )
            obj.quantity += new_receive_item.quantity
            obj.save()
        return receive
