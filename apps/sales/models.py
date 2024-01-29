from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField(default="")


class SaleItem(models.Model):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE)
    amount = models.FloatField(default=0)

    sale = models.ForeignKey(
        Sale, on_delete=models.CASCADE, related_name='sale_items')  # For
