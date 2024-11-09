from django.db import models

from coach_app.accounts.choices import AccountsLicenceChoices
from coach_app.accounts.models import AppUser


class Profile(models.Model):
    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    club = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to='accounts/',
    )

    license = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        choices=AccountsLicenceChoices.choices
    )

