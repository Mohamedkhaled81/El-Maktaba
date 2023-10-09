from django import forms
from .models import Contact 

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'