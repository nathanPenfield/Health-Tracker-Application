from django.contrib import admin
from .models import Symptom

@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ['name', 'severity', 'date']
    list_filter = ['name', 'severity', 'date']
