from django.urls import path
from .views import mainView, dashboardView, customerView

urlpatterns = [
    path('', mainView, name='mainView'),
    path('home/', dashboardView, name='dashboardView'),
    path('customerView/', customerView, name='customerView'),
]