from django.contrib import admin
from .models import Medication

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'dosage', 'frequency', 'start_date']
    list_filter = ['user', 'frequency', 'start_date']
