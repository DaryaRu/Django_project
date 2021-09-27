from django.contrib import admin
from shop.models.category import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Category, CategoryAdmin)