
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.core import serializers

from core.settings import USER_LIST_JSON_DIR
from .forms import CustomUserCreationForm
from .models import CustomUser

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('index')  # Change 'index' to your desired redirect path
        else:
            print(username)
            print(password)
            print("muvaffaqiyatsiz")
            messages.error(request, 'Invalid email or password.')

    return render(request, 'register/sign-in.html')  # Change 'your_app' to your app name

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password1')  # Kiritilgan parolni olish
            form.instance.set_password(password)  # Parolni hashlash
            form.instance.password_save = password  # password_save ga matn korinishida saqlash
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/sign-up.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('login')  # Foydalanuvchi avtorizatsiyadan chiqqandan so'ng o'tkaziladigan URL

def students_list_view(request):
    return render(request, 'app/users/students.html')


def employees_list_view(request):
    return render(request, 'app/users/employees.html')


def student_statistics(request):
    return render(request, 'app/users/student_statistics.html')


def employee_statistics(request):
    return render(request, 'app/users/employee_statistics.html')


