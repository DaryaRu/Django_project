from django.db import models
from django.db.models.deletion import CASCADE
from .category import Category

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=CASCADE)
    name = models.CharField(max_length=80, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
        ordering = ['name']
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name