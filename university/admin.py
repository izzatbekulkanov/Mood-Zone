from django.contrib import admin
from .models import Education, Departament, Faculty, Major, Group

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'head', 'phone_number', 'website']
    search_fields = ['name', 'code', 'phone_number']
    list_filter = ['head']

    def get_head_full_name(self, obj):
        return f"{obj.head.first_name} {obj.head.last_name}"
    get_head_full_name.short_description = 'Head'

@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'head', 'created_at', 'updated_at']
    search_fields = ['name', 'role']
    list_filter = ['head', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

    def get_head_full_name(self, obj):
        return f"{obj.head.first_name} {obj.head.last_name}"
    get_head_full_name.short_description = 'Head'

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'head', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['head', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

    def get_head_full_name(self, obj):
        return f"{obj.head.first_name} {obj.head.last_name}"
    get_head_full_name.short_description = 'Head'

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['faculty', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'major', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['major', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
