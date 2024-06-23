from django.db import models

from apps.products.models import Product


class Receive(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()


class ReceiveItem(models.Model):
    receive = models.ForeignKey(
        Receive, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
