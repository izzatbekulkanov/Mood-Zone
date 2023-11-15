from django.urls import path
from .views import mainView, studentView

urlpatterns = [
    path('', mainView, name='main'),
    path('', studentView, name='studentView'),
    ]
