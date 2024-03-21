# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.shortcuts import render



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
            print("muvaffaqiyatsiz")
            messages.error(request, 'Invalid email or password.')
    return render(request, 'register/login.html')  # Change 'your_app' to your app name


def role_view(request):
    return render(request, 'pages/roles.html')

def permission_view(request):
    return render(request, 'pages/permissions.html')


def create_student(request):
    return render(request, 'app/university/pages/create_student.html')



def student_list(request):
    return render(request, 'app/university/pages/student_list.html')
