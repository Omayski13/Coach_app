from cloudinary.uploader import destroy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.core.exceptions import PermissionDenied

from coach_app.accounts.forms import AppUserCreationForm, AppUserEditForm, AppUserLoginForm
from coach_app.accounts.models import AppUser, Profile
from coach_app.common.mixins import DeleteCloudinaryFormValidMixin
from coach_app.drills.mixins import DrillFiltersMixin
from coach_app.drills.models import Drill
from coach_app.drills.views import DrillDashboardView


# Create your views here.

class UserRegisterVIew(CreateView):
    form_class = AppUserCreationForm
    template_name = 'accounts/accounts-register.html'
    success_url = reverse_lazy('home-page')


class UserLoginView(LoginView):
    authentication_form = AppUserLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home-page')

        return super().dispatch(request, *args, **kwargs)


class UserDetailsView(LoginRequiredMixin,DetailView):
    template_name = 'accounts/accounts-details.html'
    model = AppUser

class UserDrillsView(DrillDashboardView,DrillFiltersMixin):
    template_name = 'accounts/accounts-drills.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_drills'] = self.request.user.drills.all()

        context['viewed_user'] = get_object_or_404(AppUser, pk=self.kwargs['pk'])

        return context
    def get_queryset(self):

        viewed_user = get_object_or_404(AppUser, pk=self.kwargs['pk'])
        queryset = Drill.objects.filter(author=viewed_user)

        return self.get_filtered_queryset(queryset)


class UserFavouritesView(DrillDashboardView, DrillFiltersMixin):
    template_name = 'accounts/accounts-favourites.html'

    def get_object(self):
        UserModel = get_user_model()
        return get_object_or_404(UserModel, pk=self.kwargs['pk'])

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user.pk != self.object.pk and not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to access this page.")

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_favourites'] = self.request.user.favorite_drills.all()

        return context

    def get_queryset(self):
        queryset = Drill.objects.filter(favorite_drills__user=self.request.user)
        return self.get_filtered_queryset(queryset)


class UserEditView(LoginRequiredMixin,DeleteCloudinaryFormValidMixin,UpdateView):
    template_name = 'accounts/accounts-edit.html'
    form_class = AppUserEditForm
    model = Profile
    cloudinary_delete_field = 'profile_picture'

    def get_success_url(self):
        return reverse_lazy(
            'user-details',
            kwargs={
                'pk':self.object.pk
            }
        )

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.pk != self.request.user.pk:
            if not self.request.user.is_superuser:
                raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['username'].initial = self.request.user.username
        return context
