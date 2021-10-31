from shop.models.cart_item import CartItem
from rest_framework import serializers
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['created_by']
