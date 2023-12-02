"""
Adjusting the configurations of users application
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """
        allow signal sending when a user is ready
        """
        import users.signals
