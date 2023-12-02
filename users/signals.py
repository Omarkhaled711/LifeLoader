"""
A signals file to automate the creation of profiles
when users are created, and the saving of profiles
when updated
"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    A method that creates profiles when a new user is created
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    A method that creates profiles when a new user is created
    """
    instance.profile.save()
