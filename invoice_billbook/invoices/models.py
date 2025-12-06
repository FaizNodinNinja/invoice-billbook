from django.db import models

# Create your models here.
from clients.models import Client
from quotations.models import Quotation

class Invoice(models.Model):
    STATUS_UNPAID = 'unpaid'
    STATUS_PAID = 'paid'
    STATUS_OVERDUE = 'overdue'

    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    quotation = models.ForeignKey(Quotation, on_delete=models.SET_NULL, null=True, blank=True)
    invoice_number = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True, null=True, default=None)

    def __str__(self):
        return self.invoice_number