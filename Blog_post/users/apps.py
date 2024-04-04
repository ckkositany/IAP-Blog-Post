from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


    #importing users signals from signals.py inside the ready function here
    def ready(self):
        import users.signals
