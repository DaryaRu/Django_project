from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop.viewsets.category_viewset import CategoriesViewSet
from shop.viewsets.product_viewset import ProductsViewSet
from shop.viewsets.user_viewset import UserCreate, UsersViewSet
from shop.viewsets.order_viewset import OrdersViewSet
from shop.viewsets.cart_item_viewset import CartItemViewSet
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'users', UsersViewSet, basename='users')
router.register(r'orders', OrdersViewSet, basename='orders')
router.register(r'cart', CartItemViewSet, basename='cart')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('account/register', UserCreate.as_view()),
    url('auth/', obtain_jwt_token),
    url('refresh/', refresh_jwt_token)
]
