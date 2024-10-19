# Create your models here.
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    # Для иконки категории (например, Bootstrap icons)
    icon = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()  # Количество на складе
    image = models.ImageField(upload_to='products/',
                              blank=True, null=True)  # Картинка продукта
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    # Флаг, чтобы определить популярные товары
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title
