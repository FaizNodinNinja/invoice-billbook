from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re  # ✅ Add this line


class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ( "first_name", "last_name", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email").lower().strip()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"].lower()
        if commit:
            user.save()
        return user

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords do not match.")

            # First letter capital check
            if not password1[0].isupper():
                raise forms.ValidationError("Password must start with a capital letter.")

            # At least one number check
            if not re.search(r"\d", password1):
                raise forms.ValidationError("Password must contain at least one number.")

            # At least one special character check (^&$^#%@)
            if not re.search(r"[\\^&$#%@]", password1):
                raise forms.ValidationError("Password must contain at least one special character (^&$^#%@).")

        return password2
