from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

from coach_app.choices import AccountsLicenceChoices
from coach_app.accounts.mixins import UserNameTextsMixin, EmailTextsMixin, Pass12TextsMixin, PasswordTextsMixin, \
    UserNameOrEmailTextsMixin, FirstNameTextsMixin, LastNameTextsMixin, ClubTextsMixin, LicenseTextsMixin, \
    UsernameCleanMethiodMixin, Pass12CleanMethodMixin
from coach_app.accounts.models import AppUser, Profile
from coach_app.common.mixins import AddAsterixToRequired, CloudinaryImageValidatorMixin


class AppUserCreationForm(AddAsterixToRequired,UserNameTextsMixin,UsernameCleanMethiodMixin, EmailTextsMixin,Pass12TextsMixin,Pass12CleanMethodMixin, UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email',]


class AppUserLoginForm(UserNameOrEmailTextsMixin,PasswordTextsMixin, AuthenticationForm):
    error_messages = {
        'invalid_login': 'Моля, въведете валидно потребителско име и парола.',
        'inactive': 'Този акаунт е неактивен.',
    }


class AppUserDetailsForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        required=True
    )

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


class AppUserEditForm(CloudinaryImageValidatorMixin,UserNameTextsMixin,FirstNameTextsMixin,LastNameTextsMixin,ClubTextsMixin,LicenseTextsMixin,forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    username = forms.CharField(
        max_length=50,
        required=True
    )

    def clean_profile_picture(self):
       return self.validate_field('profile_picture')

    def clean_username(self):
        username = self.cleaned_data['username']
        if AppUser.objects.filter(username=username).exists() and self.instance.user.username != username:
            raise ValidationError('Това потребителско име вече е заето.')
        return username

    def save(self, commit=True):
        profile = super().save(commit=False)
        username = self.cleaned_data.get('username')
        if username:
            profile.user.username = username
            profile.user.save()
        if commit:
            profile.save()
        return profile

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_order = ['username', 'first_name', 'last_name', 'club', 'license','profile_picture']
        ordered_fields = {field: self.fields[field] for field in field_order if field in self.fields}
        self.fields = ordered_fields









