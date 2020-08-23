from django.apps import AppConfig


# Users app configuration
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
