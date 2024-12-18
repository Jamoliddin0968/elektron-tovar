from django.db import models

from apps.products.models import Product


class Receive(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.User", on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    comment = models.TextField(default="")


class ReceiveItem(models.Model):
    receive = models.ForeignKey(
        Receive, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
