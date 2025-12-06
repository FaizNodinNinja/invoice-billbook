from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['invoice', 'payment_date', 'amount', 'method', 'reference_number', 'note']
