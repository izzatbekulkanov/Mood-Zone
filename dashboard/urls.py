from django.urls import path
from .views import index, statis, privacy_view, interactive_services, edu_services, administrator_services, error_page

urlpatterns = [
    path('', index, name='index'),
    path('administrator/', administrator_services, name='administrator_services'),
    path('static_dashboard', statis, name='statics_dashboard'),
    path('privacy_view', privacy_view, name='privacy_view'),
    path('interactive_services', interactive_services, name='interactive_services'),
    path('edu_services', edu_services, name='edu_services'),
    path('error_page', error_page, name='error'),
    # path('weather', weather, name='weather'),
]
