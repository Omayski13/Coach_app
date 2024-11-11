from django.core.validators import MinValueValidator
from django.db import models

from coach_app.choices import AccountsLicenceChoices, AgeGroupsChoices


# Create your models here.

class Listing(models.Model):
    club = models.CharField(
        max_length=50,
    )

    experience_needed = models.PositiveSmallIntegerField()

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
        validators=[MinValueValidator(10)],
    )


