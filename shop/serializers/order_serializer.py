from shop.models.order_item import OrderItem
from shop.models.order import Order
from shop.models.order import Order
from shop.models.order_item import OrderItem
from rest_framework import serializers

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'