"""
Extending the existing user model with custom
made functionalities.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    add a profiel model to the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """
        A __str__ method to be descriptive about the objects of this model
        """
        return f'{self.user.username} profile'
