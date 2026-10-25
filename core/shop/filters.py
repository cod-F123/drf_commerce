import django_filters
from django.db.models import Q
from .models import Product

class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method= "search_product",
        label="search product"
    )
    
    filter_q = django_filters.CharFilter(
        method="filtered_by_category_name",
        label="filter by category"
    )
    
    o_off = django_filters.BooleanFilter(
        method="ordered_by_offerd",
        label="more offerd"
    )
    
    
    def search_product(self, queryset,name, value):
        return queryset.filter(Q(name__icontains = value) | Q(description__icontains = value) | Q(category__name__icontains = value))
    
    def filtered_by_category_name(self, queryset, name, value):
        return queryset.filter(Q(category__name = str(value)))
    
    def ordered_by_offerd(self, querset, name, value):
        return querset.all().order_by("-percent_off") if value==True else querset.all()

    
    class Meta:
        model = Product
        fields = []