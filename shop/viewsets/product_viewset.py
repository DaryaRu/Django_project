from shop.models.product import Product
from rest_framework import viewsets
from shop.serializers.product_serializer import ProductSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
