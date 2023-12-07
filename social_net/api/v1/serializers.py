"""
A serializer to define how the model data should be converted to JSON.
"""
from rest_framework import serializers
from social_net.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    serializer for the Post model
    """
    date_created = serializers.SerializerMethodField()

    def get_date_created(self, obj):
        return obj.date_created.strftime("%d-%m-%Y %H:%M")

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'date_created']
