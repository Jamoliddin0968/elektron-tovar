from django.db import models

from apps.receives.models import ReceiveItem


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
