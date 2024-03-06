from django.urls import path
from .views import (
    university_dashboard, login)

urlpatterns = [
    path('', university_dashboard, name='university_dashboard'),

]
