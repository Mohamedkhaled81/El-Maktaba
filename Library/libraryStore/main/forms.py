from django import forms
from .models import Contact 

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'mssg': forms.Textarea(attrs={'rows':7, 'cols': 40}),  # Customize the text area
        }