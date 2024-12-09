from difflib import SequenceMatcher

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import MinimumLengthValidator as BaseMinimumLengthValidator, \
    UserAttributeSimilarityValidator
from django.contrib.auth.password_validation import CommonPasswordValidator as BaseCommonPasswordValidator
from django.contrib.auth.password_validation import NumericPasswordValidator as BaseNumericPasswordValidator

class CustomMinimumLengthValidator(BaseMinimumLengthValidator):
    def __init__(self, min_length=8):
        super().__init__(min_length=min_length)

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _('Паролата трябва да бъде поне %(min_length)d символа.') % {'min_length': self.min_length},
                code='password_too_short',
            )


class CustomCommonPasswordValidator(BaseCommonPasswordValidator):
    def validate(self, password, user=None):
        # Use the preloaded list of common passwords
        if password.lower() in self.passwords:
            raise ValidationError(
                _('Тази парола е твърде често срещана.'),  # Custom error message in Bulgarian
                code='password_too_common',
            )


class CustomNumericPasswordValidator(BaseNumericPasswordValidator):
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _('Паролата не може да бъде само цифри.'),
                code='password_entirely_numeric',
            )


class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def validate(self, password, user=None):
        if not user:
            return

        # Attributes to check against
        attributes = ['username', 'first_name', 'last_name', 'email']
        for attribute_name in attributes:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, str):
                continue

            # Check similarity using SequenceMatcher
            similarity = SequenceMatcher(a=password.lower(), b=value.lower()).ratio()
            if similarity > 0.7:  # Threshold for similarity (adjust as needed)
                raise ValidationError(
                    "Паролата не трябва да бъде твърде подобна на потребителското име.",  # Custom message in Bulgarian
                    code='password_too_similar',
                )