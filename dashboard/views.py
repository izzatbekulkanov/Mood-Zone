from datetime import datetime
from django.contrib.sites import requests
from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='users:sign_in')
def dashboardView(request):
    return render(request, 'dashboard/main.html')

@login_required(login_url='users:sign_in')
def adminPage(request):
    return render(request, 'dashboard/admin.html')

@login_required(login_url='users:sign_in')
def blankPage(request):
    return render(request, 'dashboard/blank-page.html')

@login_required(login_url='users:sign_in')
def userView(request):
    return render(request, 'home/users.html')

@login_required(login_url='users:sign_in')
def inboxView(request):
    return render(request, 'email/inbox.html')

@login_required(login_url='users:sign_in')
def iconSolidView(request):
    return render(request, 'icons/solid.html')

@login_required(login_url='users:sign_in')
def iconOutlineView(request):
    return render(request, 'icons/outline.html')

@login_required(login_url='users:sign_in')
def iconDualToneView(request):
    return render(request, 'icons/dual-tone.html')


