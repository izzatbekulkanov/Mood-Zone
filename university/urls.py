from django.urls import path
from .views import (
    university_dashboard, departments, save_departments_from_api, get_departments, )

urlpatterns = [
    path('', university_dashboard, name='university_dashboard'),
    path('department', departments, name='departments'),
    path('save_department', save_departments_from_api, name='save_department'),
    path('get_departments/', get_departments, name='get_departments/'),

]
