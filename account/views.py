# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import redirect, HttpResponse


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


@login_required
def add_student(request):
    return render(request, 'app/users/create_student.html')


def students_list_view(request):
    return render(request, 'app/users/students.html')


def employees_list_view(request):
    return render(request, 'app/users/employees.html')


def student_statistics(request):
    return render(request, 'app/users/student_statistics.html')


def employee_statistics(request):
    return render(request, 'app/users/employee_statistics.html')


def university_dashboard(request):
    return render(request, 'app/university/layout/index.html')
