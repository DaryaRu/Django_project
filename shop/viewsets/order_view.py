from shop.models.order import Order
from rest_framework import viewsets
from shop.serializers.order_serializer import OrderSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
