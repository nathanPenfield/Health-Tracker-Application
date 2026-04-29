from django.db import models
from accounts.models import CustomUser

class Exercise(models.Model):
    TYPE_CHOICES = [
        ('Run', 'Run'),
        ('Walk', 'Walk'),
        ('Lifting', 'Weight Lifting'),
        ('Bike','Biking'),
        ('Swim','Swim'),
        ('Other','Other'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    date = models.DateField()
    notes = models.TextField(blank=True)
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"