from django.core.exceptions import ValidationError


class UserNameTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].required = True
        self.fields['username'].label = "Потребителско име"
        self.fields['username'].help_text = ""
        self.fields['username'].widget.attrs.update({
            'placeholder': "Въведи потребителско име...",
            'class': 'wide-input'
        })
        self.fields['username'].error_messages = {
            'required': 'Моля, въведете потребителско име.',
            'invalid': 'Невалидно потребителско име. Използвайте само букви, цифри и символите @/./+/-/_',
            'unique': 'Това потребителско име вече е заето.',
        }


class UsernameCleanMethiodMixin():
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and self.Meta.model.objects.filter(username=username).exists():
            raise ValidationError(self.fields['username'].error_messages['unique'])
        return username


class UserNameOrEmailTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].required = True
        self.fields['username'].label = "Потр. име или имейл"
        self.fields['username'].help_text = ""
        self.fields['username'].widget.attrs.update({
            'placeholder': "Въведи потр. име или имейл...",
            'class': 'wide-input'
        })


class PasswordTextsMixin():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].required = True
        self.fields['password'].label = "Парола"
        self.fields['password'].widget.attrs.update({
            'placeholder': "Въведи парола...",
            'class': 'wide-input'
        })


class EmailTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['email'].label = "Имейл"
        self.fields['email'].widget.attrs.update({
            'placeholder': "Въведи валиден имейл...",
            'class': 'wide-input'
        })

        self.fields['email'].error_messages = {
            'required': 'Моля, въведете имейл адрес.',
            'invalid': 'Невалиден имейл адрес.',
            'unique': 'Потребител с този имейл вече е регистриран.',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and self.Meta.model.objects.filter(email=email).exists():
            raise ValidationError(self.fields['email'].error_messages['unique'])
        return email


class Pass12TextsMixin():
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].required = True
        self.fields['password1'].help_text = "Паролата не може да бъда само цифри и трябва да бъде поне 8 символа"
        self.fields['password1'].label = "Парола"
        self.fields['password1'].widget.attrs.update({
            'placeholder': "Въведи парола...",
            'class': 'wide-input'
        })

        self.fields['password2'].required = True
        self.fields['password2'].help_text = ''
        self.fields['password2'].label = 'Потвърди парола'
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Повтори парола...',
            'class': 'wide-input'
        })


class Pass12CleanMethodMixin:
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            # Check if passwords match
            if password1 != password2:
                self.add_error('password2', 'Паролите не съвпадат.')

            # Additional password validations
            if len(password1) < 8:
                self.add_error('password1', 'Паролата трябва да бъде поне 8 символа.')
            if password1.isdigit():
                self.add_error('password1', 'Паролата не може да бъде само цифри.')
            if not any(char.isdigit() for char in password1):
                self.add_error('password1', 'Паролата трябва да съдържа поне една цифра.')
            if not any(char.isupper() for char in password1):
                self.add_error('password1', 'Паролата трябва да съдържа поне една главна буква.')
            if not any(char.islower() for char in password1):
                self.add_error('password1', 'Паролата трябва да съдържа поне една малка буква.')
            if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password1):
                self.add_error('password1', 'Паролата трябва да съдържа поне един специален символ.')

        return cleaned_data


class FirstNameTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Име'
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Въведи Име...',
            'class': 'wide-input'
        })

class LastNameTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].label = 'Фамилия'
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Въведи Фамилия...',
            'class': 'wide-input'
        })
class ClubTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['club'].label = 'Име на отбор'
        self.fields['club'].widget.attrs.update({
            'placeholder': 'Въведи отбор...',
            'class': 'wide-input'
        })
class LicenseTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['license'].label = 'Лиценз'
        self.fields['license'].widget.attrs.update({
            'class': 'wide-input'
        })
