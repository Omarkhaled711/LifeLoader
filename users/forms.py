"""
Customize The registration form.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class UserRegistrationForm(UserCreationForm):
    """
    Add an Email field to the form
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    Update user info
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    update profile info
    """
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']

    def __init__(self, *args, **kwargs):
        """ Set required to False for the 'bio' field """
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['bio'].required = False
