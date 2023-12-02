from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import CustomUser
from django import forms

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




def signUpView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.email}")

    context = {}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name').lower()
            last_name = form.cleaned_data.get('last_name').lower()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')

            # Parolni va emailni tekshirish
            try:
                validate_password(raw_password, user=email)
            except forms.ValidationError as e:
                form.add_error('password1', e)
                context['registration_form'] = form
                messages.error(request, 'There was an error with your submission. Please correct the errors below.')
                return render(request, 'auth-pro/sign-up.html', context)

            account = authenticate(email=email, password=raw_password, first_name=first_name, last_name=last_name, username=username)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect('dashboard')
        else:
            # Formda xato mavjud, xatolarni konsolga chiqaring
            print(form.errors)
            context['registration_form'] = form
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'auth-pro/sign-up.html', context)


@login_required(login_url='sign_in')
def lockScreenView(request):
    if request.method == 'POST':
        password = request.POST.get('lock-pass')
        user = authenticate(request, username=request.user.username, password=password, backend='django.contrib.auth.backends.ModelBackend')

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

