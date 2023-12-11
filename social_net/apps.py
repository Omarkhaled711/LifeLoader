from django.apps import AppConfig


class SocialNetConfig(AppConfig):
    """
    Configuration class for the 'social_net' Django app.

    This class defines the configuration for the 'social_net' app, specifying the default auto field
    and the name of the app.

    Attributes:
        - default_auto_field: The default auto field for model primary keys.
        - name: The name of the Django app, which is 'social_net' in this case.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social_net'
