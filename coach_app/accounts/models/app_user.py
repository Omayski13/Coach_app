from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser, User
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
        # error_messages={
        #     "unique": _("Това потребителско име вече е заето."),
        # },
    )
    email = models.EmailField(
        unique=True,
        # error_messages={
        #     "unique": _("Потребител с този имейл вече е регистриран"),
        # },
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = AppUserManager()


