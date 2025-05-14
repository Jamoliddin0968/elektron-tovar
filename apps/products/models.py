import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_("Nomi"), max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items")
    description = models.TextField(_("Ma'lumot"))
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = _("Mahslulot")
        verbose_name_plural = _("Mahsulotlar")

    def __str__(self) -> str:
        return self.name
