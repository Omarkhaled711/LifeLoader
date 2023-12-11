from django.contrib.auth.models import User
from rest_framework import generics
from users.models import Profile
from users.api.v1.serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework import status


class ProfileListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating profiles.

    - `GET`: Retrieve a list of all profiles.
    - `POST`: Create a new profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveAPIView):
    """
    API view for retrieving a specific profile.

    - `GET`: Retrieve the profile for a given user ID.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve the profile for the specified user ID.
        """
        try:
            user_id = kwargs['user_id']
            # Use user__id to filter by user_id
            profile = Profile.objects.get(user__id=user_id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
