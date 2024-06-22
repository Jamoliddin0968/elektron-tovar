# Create your models here.
from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    secondname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.firstname} {self.secondname}"
