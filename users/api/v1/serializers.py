from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer is used to convert User model instances into JSON
    representation. It includes fields such as id, username, and email.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.

    This serializer includes a nested UserSerializer to represent the user
    associated with the profile. It converts Profile model instances into
    JSON representation, including fields such as user, bio, and profile_pic.
    """
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'profile_pic')
