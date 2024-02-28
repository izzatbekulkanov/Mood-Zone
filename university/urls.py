from django.urls import path
from .views import (faculty_list,
                    department_list,
                    managment_list,
                    university_dashboard,)

urlpatterns = [
    path('', university_dashboard, name='university_dashboard'),
    path('faculty/', faculty_list, name='faculty'),
    path('departament/', department_list, name='departament'),
    path('managment/', managment_list, name='managment'),
]
