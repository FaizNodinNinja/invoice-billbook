from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['company', 'category', 'amount', 'date', 'description', 'receipt']
