from users.models import Profile
from social_net.models import Post, Comment, Like
from django.contrib.auth.models import User
from django.utils.functional import SimpleLazyObject


class RouterClass:
    def db_for_read(self, model, **hints):
        return 'read_replica'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if objects are in the same database
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Allow migrations on the default database
        return db == 'default'

    def _get_database(self, obj):
        return getattr(obj, '_state', None).db or 'default'
