from django.contrib import admin

# Register your models here.
from .models import Sale, SaleItem

admin.site.register((Sale, SaleItem))
