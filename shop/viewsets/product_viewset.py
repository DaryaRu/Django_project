from shop.models.product import Product
from rest_framework import viewsets
from shop.serializers.product_serializer import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as drf_filters
from rest_framework import filters

class ProductFilter(drf_filters.FilterSet):
    min_price = drf_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = drf_filters.NumberFilter(field_name="price", lookup_expr='lte')
    # name = filters.CharFiels
    class Meta:
        model = Product
        fields = ['category', 'available']

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['name']
