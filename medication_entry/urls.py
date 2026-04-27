from django.urls import path
from . import views

app_name = 'medication_entry'

urlpatterns = [
    path('new/', views.MedicationView, name='entry'),
    path('medications/', views.MedicationListView.as_view(), name='medication_list'),
]
