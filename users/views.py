from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import CustomUser

# Create your views here.


def usersListView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/app/user-list.html', context)
def usersAddView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/app/user-add.html', context)
def usersPrivacyView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/app/user-privacy-setting.html', context)
def usersProfileView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/app/user-profile.html', context)

def signInVIew(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/auth-pro/sign-in.html', context)


def signUpView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/auth-pro/sign-up.html', context)
def lockScreenView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/auth-pro/lock-screen.html', context)

def resetPasswordView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/auth-pro/reset-password.html', context)

