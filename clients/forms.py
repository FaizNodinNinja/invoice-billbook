from django import forms
from .models import *


class ClientFrom(forms.ModelForm):
    class Meta:
        model= Client
        fields= '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Name',
                'required': 'required', 'style': 'color: #000;'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Enter your Email',
                'required': 'required', 'style': 'color: #000;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Phone Number',
                'required': 'required', 'style': 'color: #000;'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',

                'style': 'color: #000;',
                'placeholder': 'Enter your company',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Address',
                'rows': 2,
                'required': 'required', 'style': 'color: #000;'
            }),
            'country': forms.Textarea(attrs={
                'class': 'form-select form-select-sm small-input',
                'required': 'required', 'style': 'color: #000;', 'placeholder': 'Country',
            })
        }

