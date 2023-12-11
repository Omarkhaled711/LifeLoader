"""
Registering the models here.
"""
from django.contrib import admin
from social_net.models import Post, Like, Comment

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
