from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):

    club = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    trophies = models.IntegerField(
        default=0,
    )



