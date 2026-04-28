from django.db import models
from accounts.models import CustomUser

class Medication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage_mg = models.PositiveIntegerField(default=0)
    times = models.JSONField(default=list, help_text="List of times in HH:MM format, e.g., ['09:00', '15:00']")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    refill = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
