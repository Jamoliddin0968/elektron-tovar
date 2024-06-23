from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.warehouses.models import WareHouseItem

from .models import Product


@receiver(post_save, sender=Product)
def create_warehouse_entry(sender, instance, created, **kwargs):
    pass
