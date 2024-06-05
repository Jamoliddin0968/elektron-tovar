from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=127)
    phone = models.CharField(max_length=21)
    address = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
