from shop.models.category import Category
from rest_framework import viewsets
from shop.serializers.category_serializer import CategorySerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
