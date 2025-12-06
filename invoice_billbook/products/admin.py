# Register your models here.
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'unit_price', 'stock')
    search_fields = ('name', 'sku')
