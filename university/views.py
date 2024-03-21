from django.shortcuts import render


def university_dashboard(request):
    return render(request, 'app/university/layout/index.html')


def departments(request):
    return render(request, 'app/university/pages/department.html')


def university_data(request):
    return render(request, 'app/university/pages/university-data.html')


def boss_list(request):
    return render(request, 'app/university/pages/boss_list.html')


def academic_group(request):
    return render(request, 'app/university/pages/academic_group.html')
