from django.contrib.auth import get_user_model
from django.db import models

from coach_app.drills.models import Drill

UserModel = get_user_model()

class Like(models.Model):
    to_drill = models.ForeignKey(
        to=Drill,
        on_delete=models.CASCADE,
        related_name='likes',
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="likes",
    )

class FavoriteDrill(models.Model):
    to_drill = models.ForeignKey(
        to=Drill,
        on_delete=models.CASCADE,
        related_name='favorite_drills',
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='favorite_drills',
    )

