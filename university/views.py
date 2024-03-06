# Create your views here.
from django.shortcuts import render



def university_dashboard(request):
    return render(request, 'app/university/layout/index.html')
