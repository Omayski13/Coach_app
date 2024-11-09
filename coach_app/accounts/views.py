from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from coach_app.accounts.forms import AppUserCreationForm
from coach_app.accounts.models import AppUser


# Create your views here.

class UserRegisterVIew(CreateView):
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home-page')


# class UserLoginView(LoginView):
#     form_class = UserLoginForm


class UserDetailsView(DetailView):
    template_name = 'accounts/details.html'
    model = AppUser



