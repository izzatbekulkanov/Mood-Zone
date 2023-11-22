from django.urls import path
from .views import dashboardView, blankPage, adminView, userView, inboxView

urlpatterns = [
    path('', dashboardView, name='dashboard'),
    path('blankPage/', blankPage, name='blankPage'),
    path('adminView/', adminView, name='adminView'),
    path('user/', userView, name='userView'),
    path('inbox/', inboxView, name='inboxView'),
]