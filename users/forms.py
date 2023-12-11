"""
Customize The registration form.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class UserRegistrationForm(UserCreationForm):
    """
    Customizes the user registration form by adding an Email field.

    Attributes:
    - `email`: An EmailField added to the form.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    Updates user information.

    Attributes:
    - `email`: An EmailField for updating the user's email.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Updates profile information.

    Attributes:
    - `bio`: A CharField for updating the user's biography.
    - `profile_pic`: An ImageField for updating the user's profile picture.

    Methods:
    - `__init__`: Initializes the form and sets 'bio' field as not required.
    """
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']

    def __init__(self, *args, **kwargs):
        """Initializes the form and sets 'bio' field as not required."""
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['bio'].required = False


class UserSearchForm(forms.Form):
    """
    Creates a search form to find users using their username.

    Attributes:
    - `username`: A CharField for entering the username to be searched.
    """
    username = forms.CharField(max_length=250, label='Search Username')
