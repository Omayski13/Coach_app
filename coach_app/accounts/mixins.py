class UserNameTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Потребителско име"
        self.fields['username'].help_text = ""
        self.fields['username'].widget.attrs.update({
            'placeholder': "Въведи потребителско име",
            'class': 'wide-input'
        })


class PasswordTextsMixin():
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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