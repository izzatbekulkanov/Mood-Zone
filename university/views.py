import requests
from .models import Department
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


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
    url = 'https://student.namspi.uz/rest/v1/data/department-list?page=1&limit=20'
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
    departments = Department.objects.all()
    data = []
    for department in departments:
        data.append({
            'name': department.name,
            'code': department.code,
            'structure_type': department.get_structure_type_display(),  # Get display value for structure type
            'parent': department.parent if department.parent else '-'  # If parent exists, get its name, otherwise '-'
        })
    return JsonResponse(data, safe=False)