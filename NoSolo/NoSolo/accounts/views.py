from django.contrib.auth import views as auth
from django.shortcuts import render

# Create your views here.
from NoSolo.accounts.forms import LoginForm


class LoginUserView(auth.LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

