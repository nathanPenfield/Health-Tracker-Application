from django import forms
from .models import Symptom

class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = ['name', 'severity', 'date', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-field'}),
            'severity': forms.Select(attrs={'class': 'form-field'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-field'}),
            'notes': forms.Textarea(attrs={'class': 'form-field'}),
        }