from django.urls import path
from .views import (
    university_dashboard, login_view, add_student)

urlpatterns = [
    path('', university_dashboard, name='university_dashboard'),
    path('login', login_view, name='login'),
    path('add/student', add_student, name='add_student'),
]
