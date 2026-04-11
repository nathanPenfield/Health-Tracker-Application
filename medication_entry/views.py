from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MedicationForm
from django.http import HttpRequest, HttpResponse


@login_required
def MedicationView(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = MedicationForm(request.POST)
        if form.is_valid():
            medication = form.save(commit=False)
            medication.user = request.user
            medication.save()
            return redirect("/")
    else:
        form = MedicationForm()

    return render(request, "medication_entry/entry.html", {"form": form})
    
"""
class MedicationListView(LoginRequiredMixin, ListView):
    model = Medication
    template_name = 'medication_entry/medication_list.html'
    context_object_name = 'medications'
    
    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)
"""