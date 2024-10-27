from django.contrib import admin

# Register your models here.
from .models import Stock, Warehouse

admin.site.register((Warehouse, Stock))
