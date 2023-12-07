"""
A serializer to define how the model data should be converted to JSON.
"""
from rest_framework import serializers
from social_net.models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    """
    serializer for the Post model
    """
    date_created = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_date_created(self, obj):
        return obj.date_created.strftime("%d-%m-%Y %H:%M")

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content',
                  'date_created', 'likes_count', 'comments_count']


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'username', 'post', 'content', 'date_created']

    def get_username(self, obj):
        return obj.user.username


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'date_created']
