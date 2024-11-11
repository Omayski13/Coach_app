from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from coach_app.choices import AccountsLicenceChoices, AgeGroupsChoices


# Create your models here.

class Listing(models.Model):
    club = models.CharField(
        max_length=50,
    )

    experience_needed = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    licence_required = models.CharField(
        max_length=30,
        choices=AccountsLicenceChoices.choices
    )

    for_age_group = models.CharField(
        max_length=30,
        choices=AgeGroupsChoices.choices,
        null=True,
        blank=True,
    )

    salary = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
    )

    contact_person = models.CharField(
        max_length=100,
    )

    telephone_number = models.CharField(
        max_length=13,
        validators=[MinLengthValidator(10)],
    )

    position = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='listings'
    )


