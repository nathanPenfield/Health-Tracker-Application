from django.shortcuts import render, redirect
from .models import Medication
from .forms import MedicationForm
from django.http import HttpRequest, HttpResponse


def MedicationView(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = MedicationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("/")
    else:
        form = MedicationForm()

    return render(request, "medication_entry/entry.html", {"form": form})

    ## what is this doing idk
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
"""
class MedicationListView(LoginRequiredMixin, ListView):
    model = Medication
    template_name = 'medication_entry/medication_list.html'
    context_object_name = 'medications'
    
    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)
"""