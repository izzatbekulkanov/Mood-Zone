import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from .models import Department, University


def university_dashboard(request):
    return render(request, 'app/university/layout/index.html')


def departments(request):
    return render(request, 'app/university/pages/department.html')


def update_or_create_department(data):
    department_id = data.get('id')
    name = data.get('name')
    code = data.get('code')
    parent = data.get('parent', None)
    active = data.get('active', False)
    structure_type = data.get('structureType', {}).get('code')

    department, created = Department.objects.update_or_create(
        id=department_id,
        defaults={
            'name': name,
            'code': code,
            'parent': parent,
            'active': active,
            'structure_type': structure_type
        }
    )

    # if not created:
    #     print(f"Department '{name}' updated successfully.")
    # else:
    #     print(f"Department '{name}' created successfully.")


def save_departments_from_api(request):
    url = 'https://student.namspi.uz/rest/v1/data/department-list?page=20&limit=200'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer cbdfefbb283db3a219a7e7dcefd620b4'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        items = data.get('data', {}).get('items', [])

        for item in items:
            update_or_create_department(item)

        return HttpResponse("Successfully fetched and saved data from the API.")
    else:
        print("Failed to fetch data from the API.")
        return HttpResponse("Failed to fetch data from the API.", status=response.status_code)


def get_departments(request):
    def data_collector(data_list, departments):
        for department in departments:
            data_list.append({
                'name': department.name,
                'code': department.code,
                'structure_type': department.get_structure_type_display(),
                'parent': department.parent if department.parent else '-',
                'is_active': department.active
            })

    fakultet = Department.objects.filter(structure_type=Department.FAKULTET)
    bolim = Department.objects.filter(structure_type=Department.BOLIM)
    kafedra = Department.objects.filter(structure_type=Department.KAFEDRA)
    boshqarma = Department.objects.filter(structure_type=Department.BOSHQARMA)
    markaz = Department.objects.filter(structure_type=Department.MARKAZ)
    rektorat = Department.objects.filter(structure_type=Department.REKTORAT)

    fakultet_data = []
    bolim_data = []
    kafedra_data = []
    boshqarma_data = []
    markaz_data = []
    rektorat_data = []

    data_collector(fakultet_data, fakultet)
    data_collector(bolim_data, bolim)
    data_collector(kafedra_data, kafedra)
    data_collector(boshqarma_data, boshqarma)
    data_collector(markaz_data, markaz)
    data_collector(rektorat_data, rektorat)

    response_data = {
        'fakultet': fakultet_data,
        'bolim': bolim_data,
        'kafedra': kafedra_data,
        'boshqarma': boshqarma_data,
        'markaz': markaz_data,
        'rektorat': rektorat_data,
    }
    return JsonResponse(response_data)


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



