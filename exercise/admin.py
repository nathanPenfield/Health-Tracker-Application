from django.contrib import admin
from .models import Exercise

@admin.register(Exercise)

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'date']
    list_filter = ['name', 'type', 'date']
