from django import forms
from .models import Medication

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'frequency', 'start_date', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
