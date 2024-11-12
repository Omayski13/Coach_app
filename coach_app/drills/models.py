from django.contrib.auth import get_user_model
from django.db import models

from coach_app.choices import FocusChoices
from coach_app.common.mixins import CreatedAtMixin, UpdatedAtMixin, ForAgeGroupMixin


# Create your models here.

class Drill(CreatedAtMixin,UpdatedAtMixin,ForAgeGroupMixin):
    graphics = models.ImageField(
        upload_to='drills',
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=50,
    )

    objectives = models.CharField(
        max_length=150,
    )

    description = models.TextField(
        max_length=500,
    )

    focus = models.CharField(
        max_length=20,
        choices=FocusChoices.choices
    )

    dimensions = models.CharField(
        # make validators between 5 and 6 chars
    )

    series = models.CharField()

    duration = models.CharField()

    coaching_points = models.TextField(
        max_length=250,
    )

    progression = models.CharField(
        max_length=150,
    )

    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='drills'
    )



