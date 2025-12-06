from django import forms
from .models import *


class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'

        widgets = {
            'client': forms.Select(attrs={
                'class': 'form-control form-control-sm small-input',
                'required': 'required',
                'style': 'color: #000;'
            }),
            'company': forms.Select(attrs={
                'class': 'form-control form-control-sm small-input',
                'required': 'required',
                'style': 'color: #000;'
            }),
            'quotation_number': forms.TextInput(attrs={
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
                'style': 'color: #000;'
            }),
            'terms': forms.Textarea(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Enter terms',
                'rows': 2,
                'style': 'color: #000;'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Additional notes',
                'rows': 2,
                'style': 'color: #000;'
            }),
            'subtotal': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Subtotal',
                'required': 'required',
                'style': 'color: #000;'
            }),
            'tax': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Tax Amount',
                'required': 'required',
                'style': 'color: #000;'
            }),
            'total': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Total Amount',
                'required': 'required',
                'style': 'color: #000;'
            }),
        }


class QuotationItemForm(forms.ModelForm):
    class Meta:
        model = QuotationItem
        fields = '__all__'


        widgets = {
            'quotation': forms.Select(attrs={
                'class': 'form-control form-control-sm small-input',
                'required': 'required',
                'style': 'color: #000;'
            }),
            'description': forms.Select(attrs={
                'class': 'form-control form-control-sm small-input',
                'required': 'required',
                'style': 'color: #000;'
            }),
            'quantity': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Quotation Number',
                'required': 'required',
                'style': 'color: #000;'
            }),
            'unit_price': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Total Amount',
                'required': 'required',
                'style': 'color: #000;'
            }),
            'total': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Total Amount',
                'required': 'required',
                'style': 'color: #000;'
            }),
        }
