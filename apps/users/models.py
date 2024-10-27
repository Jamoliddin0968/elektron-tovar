from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    warehouse = models.ForeignKey(
        "warehouses.Warehouse", on_delete=models.RESTRICT, null=True, blank=True
    )
