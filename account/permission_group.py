from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models

class PermissionGroup(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name

    def add_permission(self, permission_name):
        content_type = ContentType.objects.get_for_model(self)
        permission = Permission.objects.get(content_type=content_type, codename=permission_name)
        self.permissions.add(permission)

# Admin uchun permission group
admin_group, _ = PermissionGroup.objects.get_or_create(name='Admin')
admin_group.add_permission('add_permission')
admin_group.add_permission('change_permission')
admin_group.add_permission('delete_permission')

# Manager uchun permission group
manager_group, _ = PermissionGroup.objects.get_or_create(name='Manager')
manager_group.add_permission('add_manager')
manager_group.add_permission('change_manager')
manager_group.add_permission('delete_manager')

# Student uchun permission group
student_group, _ = PermissionGroup.objects.get_or_create(name='Student')
student_group.add_permission('view_student_profile')

# Teacher uchun permission group
teacher_group, _ = PermissionGroup.objects.get_or_create(name='Teacher')
teacher_group.add_permission('view_teacher_profile')

# Librarian uchun permission group
librarian_group, _ = PermissionGroup.objects.get_or_create(name='Librarian')
librarian_group.add_permission('view_library_books')
