from django.urls import path

from .university_views import save_university_from_api, get_universities_data, save_specialty_from_api, \
    save_curriculum_from_api, save_group_from_api
from .views import (
    university_dashboard, departments, save_departments_from_api, get_departments, create_student, university_data,
    student_list, boss_list, )

other_urlpatterns = [
    path('', university_dashboard, name='university_dashboard'),
    path('department', departments, name='departments'),
    path('create_student', create_student, name='create_student'),
    path('save_department', save_departments_from_api, name='save_department'),
    path('get_departments', get_departments, name='get_departments'),
    path('university_data', university_data, name='university_data'),
    path('student_list', student_list, name='student_list'),
    path('boss_list', boss_list, name='boss_list'),
]
university_url_patterns = [

    path('save_university_from_api', save_university_from_api, name='save_university_from_api-university'),
    path('save_specialty_from_api', save_specialty_from_api, name='save_specialty_from_api-university'),
    path('save_curriculum_from_api', save_curriculum_from_api, name='save_curriculum_from_api-university'),
    path('save_group_from_api', save_group_from_api, name='save_group_from_api-university'),
    path('get_universities_data', get_universities_data, name='get_universities_data'),

]

urlpatterns = other_urlpatterns + university_url_patterns
