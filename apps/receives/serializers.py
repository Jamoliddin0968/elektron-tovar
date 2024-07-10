from rest_framework import serializers

from apps.warehouses.models import WareHouseItem

from .models import Receive, ReceiveItem


class ReceiveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiveItem
        fields = ['product', 'amount', 'price', 'selling_price']


class ReceiveSerializer(serializers.ModelSerializer):
    items = ReceiveItemSerializer(many=True)

    class Meta:
        model = Receive
        fields = ['id', 'comment', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        receive = Receive.objects.create(**validated_data)
        for item_data in items_data:
            new_receive_item = ReceiveItem.objects.create(
                receive=receive, **item_data)
            WareHouseItem.objects.create(
                receive_item=new_receive_item,
                product=new_receive_item.product,
                price=new_receive_item.selling_price,
                amount=new_receive_item.amount
            )
        return receive
