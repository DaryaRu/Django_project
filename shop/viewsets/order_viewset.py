from rest_framework.exceptions import ValidationError
from shop.models.order_item import OrderItem
from shop.models.cart_item import CartItem
from shop.models.order import Order
from rest_framework import viewsets, status
from shop.serializers.order_serializer import OrderSerializer
from rest_framework.response import Response

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart_items = CartItem.objects.filter(created_by=request.user)

        if len(cart_items) == 0:
            raise ValidationError({'data': 'Корзина пуста'})

        order = serializer.save()

        for x in cart_items:
            order_item = OrderItem(quantity=x.quantity,
                                   product=x.product, order=order)
            order_item.save()

        cart_items.delete()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
