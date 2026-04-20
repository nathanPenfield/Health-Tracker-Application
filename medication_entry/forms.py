from django import forms
from .models import Medication

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'frequency', 'start_date', 'notes', 'refill']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-field'}),
            'dosage': forms.TextInput(attrs={'class': 'form-field'}),
            'frequency': forms.TextInput(attrs={'class': 'form-field'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-field'}),
            'notes': forms.Textarea(attrs={'class': 'form-field'}),
            'refill': forms.NumberInput(attrs={'class': 'form-feild', 'min': 0})
        }
