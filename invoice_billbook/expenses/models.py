# Create your models here.

from django.db import models
from companies.models import Company

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('office', 'Office'),
        ('travel', 'Travel'),
        ('salary', 'Salary'),
        ('maintenance', 'Maintenance'),
        ('other', 'Other'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    receipt = models.FileField(upload_to='expense_receipts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category} - ₹{self.amount}"
