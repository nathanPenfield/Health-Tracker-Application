from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("firstName","lastName","email","password1","password2")
    
    def clean_firstName(self):
        first_name = self.cleaned_data.get('firstName', '')
        return first_name.capitalize()
    
    def clean_lastName(self):
        last_name = self.cleaned_data.get('lastName', '')
        return last_name.capitalize()
    