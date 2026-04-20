from django.urls import path
from . import views

app_name = 'symptom_log'

urlpatterns = [
    path('new/', views.SymptomLogView, name='entry'),
]
