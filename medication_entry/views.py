from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MedicationForm
from django.http import HttpRequest, HttpResponse
from .models import Medication
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

@login_required
def MedicationView(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = MedicationForm(request.POST)
        if form.is_valid():
            medication = form.save(commit=False)
            medication.user = request.user
            medication.times = form.cleaned_data['times']
            medication.save()
            return redirect("/")
    else:
        form = MedicationForm()

    return render(request, "medication_entry/entry.html", {"form": form})
    
class MedicationListView(LoginRequiredMixin, ListView):
    model = Medication
    template_name = 'medication_entry/medication_list.html'
    context_object_name = 'medications'
    
    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

def HomeView(request: HttpRequest) -> HttpResponse:
    context = {}
    notifications = []
    if request.user.is_authenticated:
        meds = Medication.objects.filter(user=request.user)
        context['meds'] = meds
        
        current_time = datetime.now().strftime("%H:%M")  
        current_hour = int(current_time[:2])-4    
        current_min = int(current_time[3:])
        for med in meds:
            if med.times:
                for time in med.times:
                        hour = int(time[:2])
                        min = int(time[3:])
                        difference = (current_hour*60 + current_min)-(hour*60 + min)
                        if difference>=0 and difference <= 60:
                            notifications.append(f"You should have taken your {med.name} medication {abs(difference)} minutes ago")    
                        elif difference<0 and difference >= -60:
                           notifications.append(f"Take your {med.name} medication in {abs(difference)} minutes")
        context['notifications'] = notifications
    return render(request, "home.html", context)
