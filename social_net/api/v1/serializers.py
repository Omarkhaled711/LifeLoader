"""
A serializer to define how the model data should be converted to JSON.
"""
from rest_framework import serializers
from social_net.models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.

    Serializes Post objects, including additional fields for formatted date_created,
    likes count, and comments count.

    Fields:
        - id: The unique identifier for the post.
        - author: The user who created the post.
        - title: The title of the post.
        - content: The content of the post.
        - date_created: The timestamp when the post was created (formatted as "%d-%m-%Y %H:%M").
        - likes_count: The count of likes received by the post.
        - comments_count: The count of comments received by the post.

    Methods:
        - get_date_created(obj): Returns the formatted date_created for the post.
        - get_likes_count(obj): Returns the count of likes received by the post.
        - get_comments_count(obj): Returns the count of comments received by the post.

    Example:
        ```
        {
            "id": 1,
            "author": 1,
            "title": "Example Post",
            "content": "This is an example post.",
            "date_created": "01-01-2023 12:34",
            "likes_count": 10,
            "comments_count": 5
        }
        ```
    """
    date_created = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    author_username = serializers.ReadOnlyField(source='author.username')
    author_profile_pic = serializers.ReadOnlyField(
        source='author.profile.profile_pic.url')

    def get_date_created(self, obj):
        """ Returns the formatted date_created for the post. """
        return obj.date_created.strftime("%d-%m-%Y %H:%M")

    def get_likes_count(self, obj):
        """ Returns the count of likes received by the post."""
        return obj.likes.count()

    def get_comments_count(self, obj):
        """ Returns the count of comments received by the post. """
        return obj.comments.count()

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'author_profile_pic', 'title', 'content',
                  'date_created', 'likes_count', 'comments_count']


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    Serializes Comment objects, including additional fields for username.

    Fields:
        - id: The unique identifier for the comment.
        - user: The user who created the comment.
        - username: The username of the user who created the comment (added using SerializerMethodField).
        - post: The post to which the comment belongs.
        - content: The content of the comment.
        - date_created: The timestamp when the comment was created.

    Methods:
        - get_username(obj): Returns the username of the user who created the comment.

    Example:
        ```
        {
            "id": 1,
            "user": 1,
            "username": "john_doe",
            "post": 5,
            "content": "Great post!",
            "date_created": "2023-01-01T12:34:56Z"
        }
        ```
    """
    username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'username', 'post', 'content', 'date_created']

    def get_username(self, obj):
        return obj.user.username


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.

    Serializes Like objects.

    Fields:
        - id: The unique identifier for the like.
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
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'date_created']
