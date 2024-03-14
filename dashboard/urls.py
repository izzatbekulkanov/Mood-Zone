from django.urls import path
from .views import index, statis, privacy_view, interactive_services, edu_services, role_view

urlpatterns = [
    path('', index, name='index'),
    path('static_dashboard', statis, name='statics_dashboard'),
    path('privacy_view', privacy_view, name='privacy_view'),
    path('interactive_services', interactive_services, name='interactive_services'),
    path('edu_services', edu_services, name='edu_services'),
    path('role_view', role_view, name='role_view'),
    # path('weather', weather, name='weather'),
]
