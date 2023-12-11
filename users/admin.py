"""
Register models to be viewed in admin panel here.
"""
from django.contrib import admin
from users.models import Profile

admin.site.register(Profile)
