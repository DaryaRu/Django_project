from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80, db_index=True)

    class Meta:
        db_table = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name