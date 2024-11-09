from django.core.exceptions import ValidationError


class UserNameTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Потребителско име"
        self.fields['username'].help_text = ""
        self.fields['username'].widget.attrs.update({
            'placeholder': "Въведи потребителско име",
            'class': 'wide-input'
        })
        self.fields['username'].error_messages = {
            'required': 'Моля, въведете потребителско име.',
            'invalid': 'Невалидно потребителско име. Използвайте само букви, цифри и символите @/./+/-/_',
            'unique': 'Това потребителско име вече е заето.',
        }
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and self.Meta.model.objects.filter(username=username).exists():
            raise ValidationError(self.fields['username'].error_messages['unique'])
        return username



class UserNameOrEmailTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Потр. име или имейл"
        self.fields['username'].help_text = ""
        self.fields['username'].widget.attrs.update({
            'placeholder': "Въведи потр. име или имейл",
            'class': 'wide-input'
        })


class PasswordTextsMixin():
    class PasswordTextsMixin():
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Set the label and widget attributes for the password field
            self.fields['password'].label = "Парола"
            self.fields['password'].widget.attrs.update({
                'placeholder': "Въведи парола",
                'class': 'wide-input'
            })


class EmailTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Имейл"
        self.fields['email'].widget.attrs.update({
            'placeholder': "Въведи валиден имейл",
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
        self.fields['password1'].help_text = "Паролата не може да бъда само цифри и трябва да бъде поне 8 символа"
        self.fields['password1'].label = "Парола"
        self.fields['password1'].widget.attrs.update({
            'placeholder': "Въведи парола",
            'class': 'wide-input'
        })

        self.fields['password2'].help_text = ""
        self.fields['password2'].label = "Потвърди парола"
        self.fields['password2'].widget.attrs.update({
            'placeholder': "Повтори парола",
            'class': 'wide-input'
        })


