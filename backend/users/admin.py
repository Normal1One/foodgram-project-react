from django.contrib import admin
from django.contrib.auth import get_user_model

from api.models import Follow

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'username',
        'first_name',
        'last_name'
    ]
    list_filter = ['email', 'username']


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'author',
    ]
    list_filter = ['user', 'author']
