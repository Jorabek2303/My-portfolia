from django import forms
from .models import ContactModel

class ContactForms(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ["name","email","subject","message"]