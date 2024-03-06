from django.urls import path
from .views import (
    university_dashboard, login_view)

urlpatterns = [
    path('', university_dashboard, name='university_dashboard'),
    path('login_view/', login_view, name='login'),

]
