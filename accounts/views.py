from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpRequest, HttpResponse

def SignUpView(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    
    return render(request, "registration/signup.html", {"form": form})
    
def LoginView(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")
    else:
        form = AuthenticationForm()
    
    return render(request, "registration/login.html", {"form": form})
    
@login_required
@require_http_methods
def SignOutView(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("/")


"""
COULD BE USEFUL LATER IF ACCOUNT VIEW ADDED
@login_required
def account_view(request: HttpRequest) -> HttpResponse:
    return render(request, "user/account.html")
"""