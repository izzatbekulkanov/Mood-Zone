from datetime import datetime
from django.contrib.sites import requests
from django.shortcuts import render
import requests


# Create your views here.

def get_student_data(page, limit, search, passport_pin, passport_number, fakultet, curriculum, group_list, gender):
    url = f"https://student.namdu.uz/rest//v1/data/student-list?page={page}&limit={limit}&_education_form=&_education_type=&_payment_form=&_department={curriculum}&_group={group_list}&_specialty=&_level=&_semester=&_province=&_district=&_gender={gender}&_citizenship=&_student_status=&search={search}&passport_pin={passport_pin}&passport_number={passport_number}"
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer F38eer5Q4FQAdCK5XVYZl698rQHR1urg',
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    students = data.get('data', {}).get('items', [])

    for student in students:
        timestamp = student.get('birth_date', 0)
        student['birth_date'] = datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y')

    return students


def get_department_data():
    url = "https://student.namdu.uz/rest//v1/data/department-list?_structure_type=&parent="
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer F38eer5Q4FQAdCK5XVYZl698rQHR1urg',
    }
    response = requests.get(url, headers=headers, data=payload)
    departments = response.json()
    fakultet = departments.get('data', {}).get('items', [])

    return fakultet


def get_curriculum_data():
    url = "https://student.namdu.uz/rest//v1/data/curriculum-list?page=1&limit=22&_department=&_education_year=&_education_type=&_education_form="
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer F38eer5Q4FQAdCK5XVYZl698rQHR1urg',
    }

    response = requests.get(url, headers=headers)
    curriculum_data = response.json()
    curriculum = curriculum_data.get('data', {}).get('items', [])

    return curriculum


def get_group_list_data():
    url = "https://student.namdu.uz/rest//v1/data/group-list?page=1&limit=200&id=&_department=&_curriculum=&_specialty=&_education_type=&_education_form="
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer F38eer5Q4FQAdCK5XVYZl698rQHR1urg',
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

        return render(request, 'api-control/api-control.html', context)

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
        #     # Topilgan ma'lumotlarni tekshirish
        #     # if not student_data and bool(search) or bool(passport_number) or bool(passport_pin):
        #     #     # Ma'lumot topilmagan holatda foydalanuvchiga xabar berish
        #     #     from django.contrib import messages
        #     #     messages.warning(request, "Ma'lumot topilmadi")
        return render(request, 'api-control/api-control.html', context)


def get_employee_data(page, limit, department, gender, staff_position, employment_form, employment_staff,
                      employee_type, academic_rank, academic_degree, passport_pin, passport_number, search):
    url = "https://student.namdu.uz/rest//v1/data/employee-list"
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer F38eer5Q4FQAdCK5XVYZl698rQHR1urg',
        'Cookie': 'PHPSESSID=vpopjdvth6p9rt3r08nblngl9c; _csrf=VIexcXQcnr0elbdHqxuZmYJTIl0yhDDj',
    }
    params = {
        'type': '',
        'page': page,
        'limit': limit,
        '_department': department,
        '_gender': gender,
        '_staff_position': staff_position,
        '_employment_form': employment_form,
        '_employment_staff': employment_staff,
        '_employee_type': employee_type,
        '_academic_rank': academic_rank,
        '_academic_degree': academic_degree,
        'passport_pin': passport_pin,
        'passport_number': passport_number,
        'search': search,
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    employees = data.get('data', {}).get('items', [])

    for employee in employees:
        timestamp = employee.get('birth_date', 0)
        employee['birth_date'] = datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y')

    return employees
def get_student_data(page, limit, search, passport_pin, passport_number, fakultet, curriculum, group_list, gender):
    url = f"https://student.namdu.uz/rest//v1/data/student-list?page={page}&limit={limit}&_education_form=&_education_type=&_payment_form=&_department={curriculum}&_group={group_list}&_specialty=&_level=&_semester=&_province=&_district=&_gender={gender}&_citizenship=&_student_status=&search={search}&passport_pin={passport_pin}&passport_number={passport_number}"
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer F38eer5Q4FQAdCK5XVYZl698rQHR1urg',
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    students = data.get('data', {}).get('items', [])

    for student in students:
        timestamp = student.get('birth_date', 0)
        student['birth_date'] = datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y')

    return students


def apiCustomerView(request):
    if request.method == 'POST':
        form = request.POST
        department = form.get('department', '')
        gender = form.get('gender', '')
        staff_position = form.get('staff_position', '')
        employment_form = form.get('employment_form', '')
        employment_staff = form.get('employment_staff', '')
        employee_type = form.get('employee_type', '')
        academic_rank = form.get('academic_rank', '')
        academic_degree = form.get('academic_degree', '')
        passport_pin = form.get('passport_pin', '')
        passport_number = form.get('passport_number', '')
        search = form.get('search', '')

        employees = get_employee_data(1, 100, department, gender, staff_position, employment_form, employment_staff,
                                      employee_type, academic_rank, academic_degree, passport_pin, passport_number,
                                      search)

        context = {
            'employees': employees,
        }

        return render(request, 'api-control/api-customers.html', context)

    else:
        return render(request, 'api-control/api-customers.html')


def apiUniversityView(request):
    url = "https://student.namdu.uz/rest//v1/public/university-list"
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer F38eer5Q4FQAdCK5XVYZl698rQHR1urg',
    }

    response = requests.get(url, headers=headers)

    try:
        university_data_list = response.json()
        first_item = university_data_list[0]
        schools = first_item.get('data', {}).get('items', [])
        print(schools)
    except (KeyError, IndexError):
        schools = []
        print(f"{schools} bosh")
        print(response.text)

    context = {
        'responce': response,
        'university': schools,
    }

    return render(request, 'api-control/api-university.html', context)
