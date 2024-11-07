from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from coach_app.accounts.forms import CustomUserForm


# Create your views here.

class UserRegisterVIew(CreateView):
    form_class = CustomUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home-page')


# class UserLoginView(LoginView):
#     form_class = UserLoginForm

