from django import forms
from .models import *
from .models import Country, State, City, Industry, IndustryType, ClientStatus

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'


        widgets = {
               'client_name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Name',
                'required': 'required' ,'style': 'color: #000;'
            }),
            'phone_no': forms.TextInput(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Phone Number',
                'required': 'required', 'style': 'color: #000;'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control form-control-sm small-input',
                'placeholder': 'Address',
                'rows': 4,
                'required': 'required', 'style': 'color: #000;'
            }),
            'industry': forms.Select(attrs={
                'class': 'form-select form-select-sm small-input',
                'required': 'required', 'style': 'color: #000;', 'placeholder': 'Select',
            }),
            'industrytype': forms.Select(attrs={
                'class': 'form-select form-select-sm small-input',
                'required': 'required', 'style': 'color: #000;', 'placeholder': 'Select',
            }),
            'country': forms.Select(attrs={
                'class': 'form-select form-select-sm small-input',
                'required': 'required', 'style': 'color: #000;', 'placeholder': 'Select',
            }),
            'state': forms.Select(attrs={
                'class': 'form-select form-select-sm small-input',
                'required': 'required', 'style': 'color: #000;', 'placeholder': 'Select',
            }),
            'city': forms.Select(attrs={
                'class': 'form-select form-select-sm small-input',
                'required': 'required','style': 'color: #000;' ,'placeholder': 'Select',
            }),
            'clientstatus': forms.Select(attrs={
                'class': 'form-select form-select-sm small-input',
                'required': 'required','style': 'color: #000;', 'placeholder': 'Select',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(LeadForm, self).__init__(*args, **kwargs)

        # Change placeholder text for dropdowns
        self.fields['industry'].empty_label = "Select"
        self.fields['industrytype'].empty_label = "Select"
        self.fields['country'].empty_label = "Select"
        self.fields['state'].empty_label = "Select"
        self.fields['city'].empty_label = "Select"
        self.fields['clientstatus'].empty_label = "Select"


class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['industry']
        widgets = {
            'Industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter industry name'})
        }

class IndustryTypeForm(forms.ModelForm):
    class Meta:
        model = IndustryType
        fields = ['industrytype']
        widgets = {
            'industrytype': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter industry type'}),
        }

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country']
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country name'})
        }

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['state']
        widgets = {
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state name'}),

        }

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city name'}),
        }

class ClientStatusForm(forms.ModelForm):
    class Meta:
        model = ClientStatus
        fields = ['clientstatus']

        widgets = {
            'clientstatus': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter client status'})
        }