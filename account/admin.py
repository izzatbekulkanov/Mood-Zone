from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, StudentType, StudentStatus, Citizenship, District, Province, Country, EmployeeType, \
    EmployeeStatus, Gender


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'email', 'full_name', 'username', 'age', 'phone_number', 'image', 'year_of_enter', 'employee_id_number',
        'gender', 'department', 'employeeStatus', 'employeeType', 'birth_date', 'is_student',
        'university', 'specialty', 'group', 'country', 'province', 'district', 'citizenship',
        'educationForm', 'educationType', 'studentType', 'studentStatus', 'curriculum',
        'passport_serial', 'passport_issue_date', 'hash', 'is_staff', 'is_active', 'user_role', 'last_login', 'date_joined'
    )
    list_filter = ('is_staff', 'is_active', 'user_role', 'gender', 'department', 'employeeStatus', 'employeeType', 'is_student', 'country', 'province', 'district', 'citizenship', 'educationForm', 'educationType', 'studentType', 'studentStatus')
    search_fields = ('email', 'full_name', 'username')
    ordering = ('email',)

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
