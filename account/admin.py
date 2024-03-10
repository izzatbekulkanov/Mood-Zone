from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, StudentType, StudentStatus, Citizenship, District, Province, Country, EmployeeType, \
    EmployeeStatus, Gender


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'full_name', 'user_role', 'is_active']
    list_filter = ['user_role', 'is_active']
    search_fields = ['username', 'email', 'full_name' 'first_name', 'last_name', 'user_role', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password' , 'password_save')}),
        ('Personal info', {'fields': ('full_name', 'user_role', 'image', 'imageFile','phone_number', 'birth_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'full_name', 'user_role', 'image', 'phone_number',
                       'birth_date', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
         ),

    )
    ordering = ['-created_at']


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(EmployeeStatus)
class EmployeeStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(EmployeeType)
class EmployeeTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(Citizenship)
class CitizenshipAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(StudentType)
class StudentTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(StudentStatus)
class StudentStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
