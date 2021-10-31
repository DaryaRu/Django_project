from django.db import models
from shop.models.product import Product
from shop.models.order import Order
from django.db.models.deletion import CASCADE

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity       
