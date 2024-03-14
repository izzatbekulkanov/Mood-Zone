from django.shortcuts import render
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def index(request):

    return render(request, 'main/index.html', )

def statis(request):
    return  render(request, 'pages/statics.html' )

def privacy_view(request):
    return  render(request, 'pages/privacy.html' )

def interactive_services(request):
    return  render(request, 'pages/interactive_services.html' )

def edu_services(request):
    return  render(request, 'pages/edu_services.html' )

def role_view(request):
    return  render(request, 'pages/roles.html' )