from django.db import models

# Create your models here.

from invoices.models import Invoice

class Payment(models.Model):
    METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('upi', 'UPI'),
        ('card', 'Card'),
        ('cheque', 'Cheque'),
        ('other', 'Other'),
    ]

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50, choices=METHOD_CHOICES, default='cash')
    reference_number = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"₹{self.amount} for {self.invoice.invoice_number} ({self.method})"
