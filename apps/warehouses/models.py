from django.db import models


class WareHouse(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.product.name
