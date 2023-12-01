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
    return render(request, 'dashboard/icons/solid.html')


def iconOutlineView(request):
    return render(request, 'dashboard/icons/outline.html')


def iconDualToneView(request):
    return render(request, 'dashboard/icons/dual-tone.html')


# def apiControlView(request):
#     page = request.GET.get('page', 500)
#     limit = request.GET.get('limit', 200)
#     search = request.GET.get('search', '')
#     passport_pin = request.GET.get('passport_pin', '')
#     passport_number = request.GET.get('passport_number', '')
#     url = f"https://student.namspi.uz/rest//v1/data/student-list?page={page}&limit={limit}&search={search}&passport_pin={passport_pin}&passport_number={passport_number}"
#     headers = {
#         'Accept': 'application/json',
#         'Authorization': 'Bearer Tw3PCq8R5KtdP6xlohOjVMzqf7_qHU-k',
#         'Cookie': 'PHPSESSID=nosq3cop5vpf0dtth3t57qhin4; _csrf=PzHVjYMd84bGQmwoAvSiQszKwHdcGhG0'
#     }
#
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     for student in data.get('data', {}).get('items', []):
#         timestamp = student.get('birth_date', 0)
#         student['birth_date'] = datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y')
#
#     student_data = data.get('data', {}).get('items', [])
#         # if data.get('data', {}).get('items', []) else None
#
#     # Topilgan ma'lumotlarni tekshirish
#     # if not student_data and bool(search) or bool(passport_number) or bool(passport_pin):
#     #     # Ma'lumot topilmagan holatda foydalanuvchiga xabar berish
#     #     from django.contrib import messages
#     #     messages.warning(request, "Ma'lumot topilmadi")
#
#     context = {
#         'student': student_data,
#         # 'searched': bool(student_data) and bool(search) or bool(passport_number) or bool(passport_pin),
#     }
#
#     # if response.status_code == 200:
#     #     # JSON ma'lumotlarni olish
#     #     users = response.json().get('data', [])
#     return render(request, 'dashboard/api-control.html', context)
#     # else:
#     #     # Xatolik sodir bo'lganda
#     #     error_message = f"Xatolik: {response.status_code}"
#     #     return render(request, 'dashboard/api-control.html', {'error_message': error_message})

def get_student_data(page, limit, search, passport_pin, passport_number, fakultet, curriculum, group_list, gender):
    url = f"https://student.namspi.uz/rest//v1/data/student-list?page={page}&limit={limit}&_education_form=&_education_type=&_payment_form=&_department={curriculum}&_group={group_list}&_specialty=&_level=&_semester=&_province=&_district=&_gender={gender}&_citizenship=&_student_status=&search={search}&passport_pin={passport_pin}&passport_number={passport_number}"
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer Tw3PCq8R5KtdP6xlohOjVMzqf7_qHU-k',
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    students = data.get('data', {}).get('items', [])

    for student in students:
        timestamp = student.get('birth_date', 0)
        student['birth_date'] = datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y')

    return students


def get_department_data():
    url = "https://student.namspi.uz/rest//v1/data/department-list?_structure_type=&parent="
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer Tw3PCq8R5KtdP6xlohOjVMzqf7_qHU-k',
    }
    response = requests.get(url, headers=headers, data=payload)
    departments = response.json()
    fakultet = departments.get('data', {}).get('items', [])

    return fakultet


def get_curriculum_data():
    url = "https://student.namspi.uz/rest//v1/data/curriculum-list?page=1&limit=22&_department=&_education_year=&_education_type=&_education_form="
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer Tw3PCq8R5KtdP6xlohOjVMzqf7_qHU-k',
    }

    response = requests.get(url, headers=headers)
    curriculum_data = response.json()
    curriculum = curriculum_data.get('data', {}).get('items', [])

    return curriculum


def get_group_list_data():
    url = "https://student.namspi.uz/rest//v1/data/group-list?page=1&limit=200&id=&_department=&_curriculum=&_specialty=&_education_type=&_education_form="
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer Tw3PCq8R5KtdP6xlohOjVMzqf7_qHU-k',
    }
    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    group_list = response.json()
    group_lists = group_list.get('data', {}).get('items', [])

    return group_lists


def apiControlView(request):
    if request.method == 'POST':
        # Form yuborilgan bo'lsa
        form = request.POST
        # Formdan kerakli ma'lumotlarni olish
        search = form.get('search', '')
        department = form.get('department', '')
        curriculum = form.get('curriculum', '')
        group_list = form.get('group_list', '')
        gender = form.get('gender', '')
        print(department)
        # Qidirish so'rovi uchun kerakli ma'lumotlarni yuborish
        students = get_student_data(1, 100, search, '', '', department, curriculum, group_list, gender)
        departments = get_department_data()
        curriculum_data = get_curriculum_data()
        group_lists = get_group_list_data()

        context = {
            'students': students,
            'departments': departments,
            'curriculum_data': curriculum_data,
            'group_lists': group_lists,
        }

        return render(request, 'dashboard/api-control.html', context)

    else:
        # Forma yuborilmagan bo'lsa
        # students = get_student_data(1, 100, '', '', '')
        departments = get_department_data()
        curriculum_data = get_curriculum_data()
        group_lists = get_group_list_data()

        context = {
            # 'students': students,
            'departments': departments,
            'curriculum_data': curriculum_data,
            'group_lists': group_lists,
        }

        return render(request, 'dashboard/api-control.html', context)


def apiCustomerView(request):
    return render(request, 'dashboard/api-customers.html')


def apiUniversityView(request):
    return render(request, 'dashboard/api-university.html')
