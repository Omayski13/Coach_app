from django.contrib.auth import get_user_model
from django.db import models

from coach_app.drills.models import Drill


class Like(models.Model):
    to_drill = models.ForeignKey(
        to=Drill,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="likes"
    )

