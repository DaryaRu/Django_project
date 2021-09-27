from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop.viewsets.category_viewset import CategoriesViewSet
from shop.viewsets.product_viewset import ProductsViewSet
from shop.viewsets.user_view import UserCreate

router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'categories', CategoriesViewSet, basename='categories')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('account/register', UserCreate.as_view())
]
