from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.warehouses.models import WareHouse

from .models import Product


@receiver(post_save, sender=Product)
def create_warehouse_entry(sender, instance, created, **kwargs):
    if created:
        obj, _ = WareHouse.objects.get_or_create(product=instance, amount=0)
