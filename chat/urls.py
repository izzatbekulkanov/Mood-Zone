from django.urls import path
from .views import dashboard
app_name = 'chat'

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
