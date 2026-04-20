from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from symptom_log.forms import SymptomForm
from .models import Symptom
from django.http import HttpRequest, HttpResponse

# Create your views here.

@login_required
def SymptomLogView(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptom_log = form.save(commit=False)
            symptom_log.user = request.user
            symptom_log.save()
            # Reload page to show updated list
            symptoms = Symptom.objects.filter(user=request.user).order_by('-created_at')
    else:
        form = SymptomForm()

    symptoms = Symptom.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "symptom_entry/entry.html", {"form": form, "symptoms": symptoms})
