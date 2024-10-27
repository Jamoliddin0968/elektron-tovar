# filters.py
import django_filters

from apps.products.models import Category

from .models import Stock


class StockFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        field_name='product__category', queryset=Category.objects.all())

    class Meta:
        model = Stock
        fields = ['category']
