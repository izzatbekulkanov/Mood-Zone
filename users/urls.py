from django.urls import path
from .views import (
    usersListView,
    signInVIew,
    signUpView,
    resetPasswordView,
    lockScreenView,
    usersAddView,
    usersPrivacyView,
    usersProfileView, user_logout,
)
app_name = 'users'

urlpatterns = [
    path('users-list/', usersListView, name='users_list'),
    path('users-add/', usersAddView, name='users_add'),
    path('users-privacy/', usersPrivacyView, name='users_privacy'),
    path('users-profile/', usersProfileView, name='users-profile'),
    path('sign-in/', signInVIew, name='sign_in'),
    path('sign-up/', signUpView, name='sign_up'),
    path('logout/', user_logout, name='user_logout'),
    path('reset-password/', resetPasswordView, name='reset_password'),
    path('lock-screen/', lockScreenView, name='lockScreen'),
]
