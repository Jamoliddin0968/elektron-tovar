from django.db import models

from apps.receives.models import ReceiveItem


class WareHouseItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    receive_item = models.ForeignKey(ReceiveItem, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.product.name
