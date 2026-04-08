from django.urls import path
from . import views

app_name = 'medication_entry'

urlpatterns = [
    path('new/', views.MedicationCreateView.as_view(), name='medication_new'),
    path('', views.MedicationListView.as_view(), name='medication_list'),
]
