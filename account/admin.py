from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'user_role', 'date_joined', 'is_staff', 'is_active']
    list_filter = ['user_role', 'date_joined', 'is_staff', 'is_active']
    search_fields = ['email', 'full_name']
    readonly_fields = ['date_joined']
    fieldsets = (
        (None, {
            'fields': (
            'email', 'password', 'first_name', 'last_name', 'full_name', 'age', 'phone_number', 'image', 'role',
            'user_role', 'is_staff', 'is_active')
        }),
        ('University Information', {
            'fields': ('passport_serial', 'passport_issue_date', 'birth_date',),
            'classes': ('collapse',)
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'password1', 'password2', 'first_name', 'last_name', 'full_name', 'age', 'phone_number', 'image',
            'role', 'user_role', 'is_staff', 'is_active')}
         ),
    )
    ordering = ['-date_joined']
