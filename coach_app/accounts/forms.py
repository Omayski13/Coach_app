from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Потребителско име"
        self.fields['username'].help_text = "Потребителско име"
        self.fields['email'].label = "Имейл"
        self.fields['password1'].label = "Парола"
        self.fields['password2'].label = "Потвърди парола"
