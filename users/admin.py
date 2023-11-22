from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'profile_picture', 'bio', 'phone_number', 'age')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    list_display = (
        'username',
        'email',
        'display_profile_picture',
        'phone_number',
        'age',
        'is_staff',
        'date_joined',
    )

    def display_profile_picture(self, obj):
        # Display profile picture as a thumbnail
        return format_html('<img src="{}" width="50" height="50" />', obj.profile_picture.url)

    display_profile_picture.short_description = 'Profile Picture'


admin.site.register(CustomUser, CustomUserAdmin)
