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
                amount=new_receive_item.amount)
        return receive
# product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
#     amount = models.PositiveIntegerField(default=0)
#     receive = models.ForeignKey(ReceiveItem, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
