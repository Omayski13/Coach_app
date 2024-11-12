from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from coach_app.choices import AccountsLicenceChoices, AgeGroupsChoices
from coach_app.common.mixins import UpdatedAtMixin, CreatedAtMixin, ForAgeGroupMixin
from coach_app.listings.validators import TelephoneValidator


# Create your models here.

class Listing(CreatedAtMixin,UpdatedAtMixin,ForAgeGroupMixin):
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

    salary = models.PositiveIntegerField(
        validators=[MinValueValidator(1, 'Заплатата трябва да бъде число по-голямо от 0')],
        null=True,
        blank=True,
    )

    contact_person = models.CharField(
        max_length=100,
    )

    telephone_number = models.CharField(
        validators=[TelephoneValidator()],
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


