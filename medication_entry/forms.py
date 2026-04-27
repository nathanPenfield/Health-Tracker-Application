from django import forms
from .models import Medication

class MedicationForm(forms.ModelForm):
    times = forms.CharField(
        help_text="Enter daily times separated by commas (e.g., 09:00, 15:00, 20:00)",
        widget=forms.TextInput(attrs={'class': 'form-field', 'placeholder': '09:00, 15:00, 20:00'}),
        required=True
    )
    
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-field'}),
        required=False
    )
    notes = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-field', 'rows': 3, 'placeholder': 'Additional notes'}),
        required=False
    )
    refill = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-field', 'min': 0, 'placeholder': 'Refills remaining'}),
        required=False
    )

    class Meta:
        model = Medication
        fields = ['name', 'dosage_mg', 'times', 'start_date', 'end_date', 'notes', 'refill']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Medication name'}),
            'dosage_mg': forms.NumberInput(attrs={'class': 'form-field', 'min': 1, 'placeholder': 'Amount in mg'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-field'}),
        }
    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if name == '':
            raise forms.ValidationError("Name must be entered")
        return name.capitalize()

    def clean_times(self):
        times_str = self.cleaned_data.get('times', '')
        if not times_str:
            raise forms.ValidationError("Times must be entered")
        
        # Parse comma-separated times and validate format
        times_list = [t.strip() for t in times_str.split(',')]
        validated_times = []
        
        for time_str in times_list:
            try:
                # Validate time format HH:MM
                parts = time_str.split(':')
                if len(parts) != 2:
                    raise forms.ValidationError("Invalid time format: must be HH:MM fomat seperated by commas. EX) 12:30,17:00")
                hour = int(parts[0])
                minute = int(parts[1])
                if not (0 <= hour <= 23 and 0 <= minute <= 59):
                    raise forms.ValidationError("Invalid time format: must be HH:MM fomat seperated by commas. EX) 12:30,17:00")
                validated_times.append(f"{hour:02d}:{minute:02d}")
            except (ValueError, IndexError):
                raise forms.ValidationError("Invalid time format: must be HH:MM fomat seperated by commas. EX) 12:30,17:00")
        
        return sorted(validated_times)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # Display times as comma-separated string for editing
            self.fields['times'].initial = ', '.join(self.instance.times) if self.instance.times else ''
