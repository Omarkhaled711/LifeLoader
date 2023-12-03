"""
Views for users app
"""
from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
