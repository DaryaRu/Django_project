from django.contrib import admin
from shop.models.product import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'available', 'description']
    list_filter = ['available']
    list_editable = ['price', 'quantity', 'available']
    
admin.site.register(Product, ProductAdmin)