"""
Extending the existing user model with custom
made functionalities.
"""
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """
    add a profiel model to the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """
        A __str__ method to be descriptive about the objects of this model
        """
        return f'{self.user.username} profile'

    def save(self):
        """
        Resizing the profile picture if it's too big.
        """
        super().save()
        # Open the uploaded image using Pillow
        img = Image.open(self.profile_pic.path)
        # Set a maximum size
        max_size = (300, 300)
        # Resize the image if it exceeds the maximum size
        if img.width > max_size[0] or img.height > max_size[1]:
            img.thumbnail(max_size)
            img.save(self.profile_pic.path)
