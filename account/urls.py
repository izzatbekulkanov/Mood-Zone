from django.urls import path

from .employeeViews import employee_views, employee_list_json, create_employee_view, get_employee_info, \
    create_employee_from_api
from .views import (login_view, create_group, group_list, edit_profile)

urlpatterns = [
    path('login', login_view, name='login'),
    path('create_group/', create_group, name='create_group'),
    path('group_list/', group_list, name='group_list'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('employee_list/', employee_views, name='employeeViews'),
    path('employee_list_json', employee_list_json, name='employee_list_json'),
    path('create_employee', create_employee_view, name='create_employee'),
    path('get_employee_info', get_employee_info, name='get_employee_info'),
    path('create_employee_from_api', create_employee_from_api, name='create_employee_from_api'),
]
