"""
Extending the existing user model with custom
made functionalities.
"""
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """
    Extends the existing user model with custom functionalities.

    Attributes:
    - `user`: One-to-one relationship with the User model.
    - `bio`: TextField for storing the user's biography.
    - `profile_pic`: ImageField for storing the user's profile picture.

    Methods:
    - `__str__`: Descriptive representation of the profile object.
    - `save`: Resizing the profile picture if it's too big.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """
        Descriptive representation of the profile object.
        """
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        """
        Resizing the profile picture if it's too big.
        """
        super().save(*args, **kwargs)
        # Open the uploaded image using Pillow
        img = Image.open(self.profile_pic.path)
        # Set a maximum size
        max_size = (300, 300)
        # Resize the image if it exceeds the maximum size
        if img.width > max_size[0] or img.height > max_size[1]:
            img.thumbnail(max_size)
            img.save(self.profile_pic.path)
