from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'first_name', 'last_name', 'age', 'phone_number', 'image', 'role', 'is_staff']
    search_fields = ['email', 'username', 'first_name', 'last_name', 'role']
    list_filter = ['is_staff', 'is_active', 'user_role']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'password_save')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'age', 'phone_number', 'image')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_role')}),
        ('University Info', {'fields': ('passport_serial', 'passport_issue_date', 'birth_date', 'group')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'password_save', 'image', 'role', 'is_staff', 'is_active', 'user_role', 'passport_serial', 'passport_issue_date', 'birth_date', 'group')}
        ),
    )
