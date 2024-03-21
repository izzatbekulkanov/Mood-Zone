from django.middleware.csrf import get_token
from django.urls import path

from .employeeViews import employee_views, employee_list_json, create_employee_view, get_employee_info, \
    create_employee_from_api
from .roleViews import group_list, create_group, group_permissions, save_group_permissions, permissions_api, \
    save_permission
from .studentViews import save_student_from_api, create_student_from_api, get_student_info
from .views import (login_view, role_view, create_student, student_list, permission_view)

login_patterns = [
    path('login', login_view, name='login'),
]

student_patterns = [
    path('save_student_from_api', save_student_from_api, name='save_student_from_api'),
    path('create_student_from_api', create_student_from_api, name='create_student_from_api'),
    path('get_student_info', get_student_info, name='get_student_info'),
    path('create_student', create_student, name='create_student'),
    path('student_list', student_list, name='student_list'),
]
employee_patterns = [
    path('employee_list/', employee_views, name='employeeViews'),
    path('employee_list_json', employee_list_json, name='employee_list_json'),
    path('create_employee', create_employee_view, name='create_employee'),
    path('get_employee_info', get_employee_info, name='get_employee_info'),
    path('create_employee_from_api', create_employee_from_api, name='create_employee_from_api'),
]

role_permissions = [
    path('role_view', role_view, name='role_view'),
    path('permissions', permission_view, name='permission_view'),
    path('group_list_api', group_list, name='group_list'),
    path('create_group_api', create_group, name='create_group'),
    path('groups/<int:group_id>', group_permissions, name='group_permissions'),
    path('groups/<int:group_id>/permissions', save_group_permissions, name='save_group_permissions'),
    path('csrf/', get_token),
    path('permissions_api', permissions_api, name='permissions_api'),
    path('save_permission', save_permission, name='save_permission'),

]

urlpatterns = login_patterns + student_patterns + employee_patterns + role_permissions
