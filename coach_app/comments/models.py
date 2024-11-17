from django.contrib.auth import get_user_model
from django.db import models

from coach_app.common.mixins import CreatedAtMixin
from coach_app.drills.models import Drill


# Create your models here.

class Comment(CreatedAtMixin):
    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]
        ordering = ['created_at']

    to_drill = models.ForeignKey(
        to=Drill,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='author',
    )

    content = models.TextField(
        max_length=300
    )





