from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ExerciseForm
from .models import Exercise
from django.http import HttpRequest, HttpResponse

# Create your views here.

@login_required
def ExerciseLogView(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
            return redirect('exercise:list')
    else:
        form = ExerciseForm()

    return render(request, "exercise/entry.html", {"form": form})

@login_required
def ExerciseListView(request: HttpRequest) -> HttpResponse:
    e = Exercise.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "exercise/list.html", {"exercises": e})

