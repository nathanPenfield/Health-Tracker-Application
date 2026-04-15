from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .models import Medication
from .forms import MedicationForm
from django.urls import reverse_lazy

class MedicationCreateView(LoginRequiredMixin, CreateView):
    model = Medication
    form_class = MedicationForm
    template_name = 'medication_entry/medication_form.html'
    success_url = reverse_lazy('medication_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MedicationListView(LoginRequiredMixin, ListView):
    model = Medication
    template_name = 'medication_entry/medication_list.html'
    context_object_name = 'medications'
    
    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)
