from django.urls import path
from .views import index, weather

urlpatterns = [
    path('', index, name='index'),
    path('weather', weather, name='weather'),
]
