from django.db import models

# Create your models here.

from clients.models import Client
from companies.models import Company

class Quotation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    quotation_number = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    due_date = models.DateField()
    terms = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quotation_number} - {self.client.name}"

class QuotationItem(models.Model):
    quotation = models.ForeignKey(Quotation, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description

