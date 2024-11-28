from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from coach_app.accounts.forms import AppUserCreationForm, AppUserEditForm
from coach_app.accounts.models import AppUser, Profile


# Create your views here.

class UserRegisterVIew(CreateView):
    form_class = AppUserCreationForm
    template_name = 'accounts/accounts-register.html'
    success_url = reverse_lazy('home-page')


# class UserLoginView(LoginView):
#     form_class = UserLoginForm


class UserDetailsView(LoginRequiredMixin,DetailView):
    template_name = 'accounts/accounts-details.html'
    model = AppUser



class UserEditView(LoginRequiredMixin,UpdateView):
    template_name = 'accounts/accounts-edit.html'
    form_class = AppUserEditForm
    model = Profile

    def get_success_url(self):
        return reverse_lazy(
            'user-details',
            kwargs={
                'pk':self.object.pk
            }
        )


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'].fields['username'].initial = self.request.user.username

        return context

    # def test_func(self):
    #     profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
    #     return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'user-details',
            kwargs={
                'pk': self.object.pk,
            }
        )


