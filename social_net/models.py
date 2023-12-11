"""
Create our database using ORM
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    """
    Model representing a post.

    Fields:
        - author: The user who created the post.
        - title: The title of the post.
        - content: The content of the post.
        - date_created: The timestamp when the post was created.
        - likes: Many-to-Many relationship with User through the Like model.
        - comments: Many-to-Many relationship with User through the Comment model.

    Methods:
        - __str__(): Returns a string representation of the post.
        - get_absolute_url(): Returns the absolute URL of the post detail view.

    Example:
        ```
        {
            "id": 1,
            "author": 1,
            "title": "Example Post",
            "content": "This is an example post.",
            "date_created": "2023-01-01T12:34:56Z",
            "likes": [...],
            "comments": [...]
        }
        ```
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
        """ Returns a string representation of the post."""
        return self.title

    def get_absolute_url(self):
        """ Returns the absolute URL of the post detail view. """
        return reverse('LifeLoader-post_detail', kwargs={'pk': self.pk})


class Like(models.Model):
    """
    Model representing a like on a post.

    Fields:
        - user: The user who created the like.
        - post: The post to which the like belongs.
        - date_created: The timestamp when the like was created.

    Example:
        ```
        {
            "id": 1,
            "user": 1,
            "post": 5,
            "date_created": "2023-01-01T12:34:56Z"
        }
        ```
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returns a string representation of the like."""
        return f'{self.user.username} likes {self.post.title}'


class Comment(models.Model):
    """
    Model representing a comment on a post.

    Fields:
        - user: The user who created the comment.
        - post: The post to which the comment belongs.
        - content: The content of the comment.
        - date_created: The timestamp when the comment was created.

    Example:
        ```
        {
            "id": 1,
            "user": 1,
            "post": 5,
            "content": "Great post!",
            "date_created": "2023-01-01T12:34:56Z"
        }
        ```
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returns a string representation of the comment."""
        return f'{self.user.username} commented on {self.post.title}'
