from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser, Role


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'get_roles')

    fieldsets = (
        ('Personal Info', {'fields': (
            'first_name', 'username', 'last_name', 'email', 'profile_image', 'profile_cover', 'phone_number', 'bio',
            'birth_of_day',
        )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'roles')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'roles'),
        }),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    def get_roles(self, obj):
        roles_html = ", ".join([role.name for role in obj.roles.all()])
        return format_html(roles_html)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'key')


admin.site.register(CustomUser, CustomUserAdmin)
