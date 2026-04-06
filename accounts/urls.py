from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView, name="signup"),
    path("login/", views.LoginView, name="login"),
    path("signout/", views.SignOutView, name="signout"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name="password_reset"),
]
