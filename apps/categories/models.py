from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=31, default="soatlar")
    description = models.CharField(max_length=255, null=True, blank=True)
