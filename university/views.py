import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from .models import Department, University


def university_dashboard(request):
    return render(request, 'app/university/layout/index.html')


def departments(request):
    return render(request, 'app/university/pages/department.html')




def create_student(request):
    return render(request, 'app/university/pages/create_student.html')


def university_data(request):
    return render(request, 'app/university/pages/university-data.html')


def users_data(request):
    return render(request, 'app/university/pages/student_list.html')

def boss_list(request):
    return render(request, 'app/university/pages/boss_list.html')

def student_list(request):
    return render(request, 'app/university/pages/student_list.html')

def academic_group(request):
    return render(request, 'app/university/pages/academic_group.html')



