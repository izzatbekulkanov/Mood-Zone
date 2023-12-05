from datetime import datetime
from django.contrib.sites import requests
from django.shortcuts import render
import requests


# Create your views here.
def dashboardView(request):
    return render(request, 'dashboard/main.html')


def adminPage(request):
    return render(request, 'dashboard/admin.html')


def blankPage(request):
    return render(request, 'dashboard/blank-page.html')


def userView(request):
    return render(request, 'home/users.html')


def inboxView(request):
    return render(request, 'email/inbox.html')


def iconSolidView(request):
    return render(request, 'icons/solid.html')


def iconOutlineView(request):
    return render(request, 'icons/outline.html')


def iconDualToneView(request):
    return render(request, 'icons/dual-tone.html')


