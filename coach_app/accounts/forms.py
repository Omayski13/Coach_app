from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

from coach_app.accounts.choices import AccountsLicenceChoices
from coach_app.accounts.mixins import UserNameTextsMixin, EmailTextsMixin, Pass12TextsMixin, PasswordTextsMixin, \
    UserNameOrEmailTextsMixin
from coach_app.accounts.models import AppUser


class AppUserCreationForm(UserNameTextsMixin,EmailTextsMixin,Pass12TextsMixin,UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email',]


class AppUserLoginForm(UserNameOrEmailTextsMixin,PasswordTextsMixin, AuthenticationForm):
    pass


class AppUserDetailsForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        required=True
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if AppUser.objects.filter(username=username).exists():
            raise ValidationError('Това потребителско име вече е заето.')
        return username

    first_name = forms.CharField(
        max_length=50,
        required=False,
    )

    last_name = forms.CharField(
        max_length=50,
        required=False,
    )

    club = forms.CharField(
        max_length=50,
        required=False,
    )

    profile_picture = forms.ImageField(
        required=False,

    )

    license = forms.ChoiceField(
        choices=AccountsLicenceChoices.choices,
        required=False,
        # label='License Type'
    )





