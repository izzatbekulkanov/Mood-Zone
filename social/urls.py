from django.urls import path
from social.views import dashboard

app_name = 'social'
urlpatterns = [
    path('', dashboard, name='dashboard')
]
