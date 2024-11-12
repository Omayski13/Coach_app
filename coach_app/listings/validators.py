from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class TelephoneValidator:
    def __init__(self,message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Полете трябва да бъде между 10 и 13 символа'
        else:
            self.__message = value

    def __call__(self,value, *args, **kwargs):
        if len(value) < 10 or len(value) > 13:
            raise ValidationError(self.message)
