from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop.viewsets.category_viewset import CategoriesViewSet
from shop.viewsets.product_viewset import ProductsViewSet
from shop.viewsets.user_view import UserCreate
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'categories', CategoriesViewSet, basename='categories')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('account/register', UserCreate.as_view()),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token)
]
