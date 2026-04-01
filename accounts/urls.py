from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView, name="signup"),
    path("login/", views.LoginView,name="login"),
    path("signout/", views.SignOutView, name= "signout"),
]