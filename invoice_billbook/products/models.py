from django.db import models

# Create your models here.


from django.db import models

class Product(models.Model):
    TYPE_CHOICES = [
        ('product', 'Product'),
        ('service', 'Service'),
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='product')
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=100, blank=True, null=True, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
