"""
Views for users app
"""
from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm
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
    return render(request, 'users/profile.html')
