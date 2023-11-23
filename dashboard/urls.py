from django.urls import path
from .views import dashboardView, adminPage, blankPage, userView, inboxView

urlpatterns = [
    path('', dashboardView, name='dashboard'),
    path('admin-page/', adminPage, name='adminPage'),
    path('blank-page/', blankPage, name='blankPage'),
    path('user/', userView, name='userView'),
    path('inbox/', inboxView, name='inboxView'),
]