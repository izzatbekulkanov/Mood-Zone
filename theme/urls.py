from django.urls import path
from .views import mainView

urlpatterns = [
    path('', mainView, name='main'),
    ]
