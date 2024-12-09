from cloudinary.uploader import destroy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.core.exceptions import PermissionDenied

from coach_app.accounts.forms import AppUserCreationForm, AppUserEditForm
from coach_app.accounts.models import AppUser, Profile
from coach_app.drills.mixins import DrillFiltersMixin
from coach_app.drills.models import Drill
from coach_app.drills.views import DrillDashboardView


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

class UserDrillsView(DrillDashboardView,DrillFiltersMixin):
    template_name = 'accounts/accounts-drills.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    def get_queryset(self):
        queryset = Drill.objects.filter(author=self.request.user)
        return self.get_filtered_queryset(queryset)


class UserFavouritesView(DrillDashboardView, DrillFiltersMixin):
    template_name = 'accounts/accounts-favourites.html'

    def get_object(self):
        # Assuming you're retrieving a user based on the 'pk' from the URL
        UserModel = get_user_model()
        return get_object_or_404(UserModel, pk=self.kwargs['pk'])

    def dispatch(self, request, *args, **kwargs):
        # Ensure `self.get_object()` retrieves the correct object
        self.object = self.get_object()

        # Check if the logged-in user is authorized
        if self.request.user.pk != self.object.pk and not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to access this page.")

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        queryset = Drill.objects.filter(favorite_drills__user=self.request.user)
        return self.get_filtered_queryset(queryset)


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

    def form_valid(self, form):
        # Get the current object before changes
        old_profile_picture = self.get_object().profile_picture

        # Save the form to apply updates
        response = super().form_valid(form)

        # If the graphics field has changed, delete the old image from Cloudinary
        new_profile_picture = self.object.profile_picture
        if old_profile_picture != new_profile_picture and old_profile_picture:
            try:
                public_id = old_profile_picture.public_id
                destroy(public_id)
            except Exception as e:
                print(f"Error deleting old graphics from Cloudinary: {e}")

        return response


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


