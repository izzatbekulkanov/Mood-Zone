from django.urls import path
from .views import usersListView

urlpatterns = [
    path('user-list/', usersListView, name='usersList'),

]