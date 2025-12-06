from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'type', 'description', 'sku', 'unit_price', 'tax_rate', 'stock']
