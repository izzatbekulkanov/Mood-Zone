from django.shortcuts import render


# Create your views here.

def university_dashboard(request):
    return render(request, 'app/university/layout/index.html')
def faculty_list(request):
    return render(request, 'app/university/faculty_list.html')

def department_list(request):

    return render(request, 'app/university/departament_list.html')

def managment_list(request):

    return render(request, 'app/university/managment_list.html')
