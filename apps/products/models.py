import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(_("Nomi"), max_length=255)
    category = models.ForeignKey(
        'categories.Category', on_delete=models.CASCADE, related_name="category_products")
    price = models.DecimalField(
        _("Sotish narxi"), decimal_places=2, max_digits=13, default=0)
    description = models.TextField(_("Ma'lumot"))

    class Meta:
        verbose_name = _("Mahslulot")
        verbose_name_plural = _("Mahsulotlar")


# class ProductImage(models.Model):
#     product = models.ForeignKey(
#         "products.product", on_delete=models.CASCADE, related_name='product_images')
#     image = models.ForeignKey(
#         "image.Image", on_delete=models.CASCADE)
