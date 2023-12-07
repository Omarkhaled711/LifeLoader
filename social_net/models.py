"""
Create our database using ORM
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    """
    The post table
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(
        User, related_name='post_likes', through='Like')
    comments = models.ManyToManyField(
        User, related_name='post_comments', through='Comment')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('LifeLoader-post_detail', kwargs={'pk': self.pk})


class Like(models.Model):
    """ likes model to handel likes on posts """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'


class Comment(models.Model):
    """ comments model to handel comments on posts """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} commented on {self.post.title}'
