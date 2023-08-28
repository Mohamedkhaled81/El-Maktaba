from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "email", "username", "password1", "password2"
        ]

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if (password != confirm_password) and password and confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return confirm_password
