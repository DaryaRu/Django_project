from django.db import models
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    class Meta:
        db_table = 'orders'
        ordering = ['-created']

    def __str__(self):
        return 'Order {}'.format(self.id)

    def total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())                
