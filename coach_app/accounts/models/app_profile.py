from django.db import models

from coach_app.choices import AccountsLicenceChoices
from coach_app.accounts.models import AppUser


class Profile(models.Model):
    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
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
        null=True,
        blank=True,
    )

    license = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        choices=AccountsLicenceChoices.choices
    )

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name and not self.last_name:
            return self.first_name
        if self.last_name and not self.first_name:
            return self.last_name

