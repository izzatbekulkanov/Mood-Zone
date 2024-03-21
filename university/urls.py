from django.urls import path

from .university_views import save_university_from_api, get_universities_data, save_specialty_from_api, \
    save_curriculum_from_api, save_group_from_api, save_departments_from_api, get_departments
from .views import (
    university_dashboard, departments, university_data,
    boss_list, academic_group, )

other_urlpatterns = [
    path('', university_dashboard, name='university_dashboard'),
    path('department', departments, name='departments'),
    path('save_department', save_departments_from_api, name='save_department'),
    path('get_departments', get_departments, name='get_departments'),
    path('university_data', university_data, name='university_data'),
    path('boss_list', boss_list, name='boss_list'),
    path('academic_group', academic_group, name='academic_group'),
]

university_users_url_patterns = [

]

university_url_patterns = [

    path('save_university_from_api', save_university_from_api, name='save_university_from_api-university'),
    path('save_specialty_from_api', save_specialty_from_api, name='save_specialty_from_api-university'),
    path('save_curriculum_from_api', save_curriculum_from_api, name='save_curriculum_from_api-university'),
    path('save_group_from_api', save_group_from_api, name='save_group_from_api-university'),
    path('get_universities_data', get_universities_data, name='get_universities_data'),

]

urlpatterns = other_urlpatterns + university_url_patterns + university_users_url_patterns
