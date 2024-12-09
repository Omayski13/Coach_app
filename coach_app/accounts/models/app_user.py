from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser, User
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from coach_app.accounts.managers import AppUserManager

class AppUser(AbstractBaseUser,PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=50,
        unique=True,
        help_text=_(
            "Задължително поле. Макс 50 символа - само букви цифри и @/./+/-/_"
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("Това потребителско име вече е заето."),
        },
    )
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": _("Потребител с този имейл вече е регистриран"),
        },
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )

    @property
    def get_lastest_drill(self):
        return self.drills.order_by('-updated_at').first()

    @property
    def get_user_tropies(self):
        return self.drills.aggregate(total_likes=Count('likes'))['total_likes'] or 0

    @property
    def get_user_comments(self):
        return self.drills.aggregate(total_comments=Count('comments'))['total_comments'] or 0

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = AppUserManager()

    def __str__(self):
        return self.username

