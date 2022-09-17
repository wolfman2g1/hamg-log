from dataclasses import fields
from django import forms
from django.core.validators import DecimalValidator
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [ 'callsign','name', 'country','state','mode', 'freq','power' ]
        labels = {
            'callsign': 'Callsign',
            'name': 'Name',
            'country': 'Country',
            'state': 'State',
            'mode': 'Mode',
            'freq': 'Frequency',
            'power': 'Power'
        }
        widgets = {

            'callsign': forms.TextInput(attrs={'class: form-control'}),
            'name': forms.TextInput(attrs={'class: form-control'}),
            'country': forms.TextInput(attrs={'class: form-control'}),
            'state': forms.TextInput(attrs={'class: form-control'}),
            'mode': forms.TextInput(attrs={'class: form-control'}),
            'freq': forms.TextInput(attrs={'class: form-control'}),
            'power': forms.TextInput(attrs={'class: form-control'})
        }