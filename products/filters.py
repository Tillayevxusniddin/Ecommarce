from django_filters import rest_framework as django_filters # pip install django-filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte") #gte katta yoki teng
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte") #lte kichik yoki teng

    class Meta:
        model = Product
        fields = ['category', 'max_price', 'min_price']

