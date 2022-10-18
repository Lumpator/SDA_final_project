from django.contrib.auth.views import LoginView
from django.urls import path

from accounts.forms import UserLoginForm
from accounts.views import signup_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", LoginView.as_view(authentication_form=UserLoginForm, template_name="registration/login.html", success_url="home"))
]

# SignUpView.as_view()