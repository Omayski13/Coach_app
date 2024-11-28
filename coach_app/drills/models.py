from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

from coach_app.choices import FocusChoices
from coach_app.common.mixins import CreatedAtMixin, UpdatedAtMixin, ForAgeGroupMixin


# Create your models here.

class Drill(CreatedAtMixin,UpdatedAtMixin,ForAgeGroupMixin):
    graphics = CloudinaryField(
        'image',
        folder='drills',  # Optional: Store images in a specific folder on Cloudinary
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

    duration = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    coaching_points = models.TextField(
        max_length=250,
        null=True,
        blank=True,
    )

    progression = models.TextField(
        max_length=150,
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='drills'
    )

    approved = models.BooleanField(
        default=False,
    )

    class Meta:
        permissions = [
            ('can_approve_drills','Can approve drills')
        ]



