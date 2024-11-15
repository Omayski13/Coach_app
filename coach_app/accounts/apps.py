from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coach_app.accounts'


    def ready(self):
        import coach_app.accounts.signals
