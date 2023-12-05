from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def usersListView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'app/user-list.html', context)


def usersAddView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'app/user-add.html', context)


def usersPrivacyView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'app/user-privacy-setting.html', context)


def usersProfileView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'app/user-profile.html', context)


def signInVIew(request):
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('dashboard')  # Change 'dashboard' to your desired redirect path
        else:
            print(username)
            print(password)
            print("muvaffaqiyatsiz")
            messages.error(request, 'Invalid email or password.')

    return render(request, 'auth-pro/sign-in.html')  # Change 'your_app' to your app name


def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('users:sign_in')

def signUpView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('users:sign_in')
    else:
        form = RegistrationForm()

    return render(request, 'auth-pro/sign-up.html', {'form': form})


@login_required(login_url='sign_in')
def lockScreenView(request):
    if request.method == 'POST':
        password = request.POST.get('lock-pass')
        user = authenticate(request, username=request.user.username, password=password,
                            backend='django.contrib.auth.backends.ModelBackend')

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully unlocked the screen.')
            return redirect('dashboard')
            print("You have successfully unlocked the screen.'")

        messages.error(request, 'Invalid password. Please try again.')
        print("Invalid password. Please try again.'")

    return render(request, 'auth-pro/lock-screen.html')  # O'zgartirilishi mumkin


def resetPasswordView(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'auth-pro/reset-password.html', context)
