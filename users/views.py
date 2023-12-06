"""
Views for users app
"""
from django.shortcuts import render, redirect, get_object_or_404
from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, UserSearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    """
    Create registeration form
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data['username']
            messages.success(
                request, f'Account succefully created for {user_name}')
            return redirect('LifeLoader-login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """
    Create a profile route for our users
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, f'Your profile has been succefully updated!')
            return redirect('LifeLoader-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    handle_forms = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', handle_forms)


@login_required
def view_profile(request, username):
    """
    View for viewing other users' profiles.
    Redirects the logged-in user to their editable profile if 
    they try to view their own profile.
    """
    viewed_user = get_object_or_404(User, username=username)

    # Check if the viewed profile belongs to the logged-in user
    if request.user == viewed_user:
        # Redirect to editable profile view
        return redirect('LifeLoader-profile')

    context = {
        'viewed_user': viewed_user,
    }
    return render(request, 'users/view_profile.html', context)


def user_search(request):
    """ View for searching about users using username """
    users = []

    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            users = User.objects.filter(username__icontains=username)

    else:
        form = UserSearchForm()
    context = {
        'form': form,
        'users': users
    }
    return render(request, 'users/user_search.html', context)
