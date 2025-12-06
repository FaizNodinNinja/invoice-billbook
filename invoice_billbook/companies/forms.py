from django import forms
from .models import *


class CompanyBusiness(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ["owner", "email"]
        labels = {
            "name": "Company Name",  # 🔴 yahan label change
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Name',
                'required': 'required',
                'style': 'color: #000;'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Email Address',
                'required': 'required',
                'style': 'color: #000;'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Phone Number',
                'required': 'required',
                'style': 'color: #000;'
            }),

            'currency': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Currency',
                'required': 'required',
                'style': 'color: #000;'
            }),

            'gst_number': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'GST Number',
                'required': 'required',
                'style': 'color: #000;'
            }),

            'logo': forms.FileInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'required': 'required',
                'style': 'color: #000;'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Address',
                'rows': 2,
                'required': 'required',
                'style': 'color: #000; height: 35px;'
            }),
        }
