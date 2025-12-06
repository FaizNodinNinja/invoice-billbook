from django import forms
from .models import *


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = '__all__'


        widgets = {
            'client': forms.Select(attrs={
                'class': 'form-control form-control-sm small-input',
                'required': 'required',
                'style': 'color: #000;'
            }),

            'quotation': forms.Select(attrs={
                'class': 'form-control form-control-sm small-input',
                'required': 'required',
                'style': 'color: #000;'
            }),

            'invoice_number': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Quotation Number',
                'required': 'required',
                'style': 'color: #000;'
            }),

            'date': forms.DateInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'type': 'date',  # Date picker
                'required': 'required',
                'style': 'color: #000;'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'type': 'date',  # Date picker
                'required': 'required',
                'style': 'color: #000;' }),

            'total_amount': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Enter Total Amount',
                'required': 'required',
                'style': 'color: #000;'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control form-control-sm small-input',
                'style': 'color: #000;'
            }),
        }