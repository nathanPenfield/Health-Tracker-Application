from django import forms
from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'type', 'date', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-field'}),
            'type': forms.Select(attrs={'class': 'form-field'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-field'}),
            'notes': forms.Textarea(attrs={'class': 'form-field'}),
        }