from shop.models.product import Product
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db import models

User = get_user_model()

class Cart(models.Model):
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'