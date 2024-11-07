from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import forms

from coach_app.accounts.mixins import UserNameTextsMixin, EmailTextsMixin, Pass12TextsMixin, PasswordTextsMixin, \
    UserNameOrEmailTextsMixin


class CustomUserForm(UserNameTextsMixin,EmailTextsMixin,Pass12TextsMixin,UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)

class CustomLoginForm(UserNameOrEmailTextsMixin,PasswordTextsMixin, AuthenticationForm):
    pass

