from datetime import datetime

import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render

from account.models import CustomUser, StudentStatus, StaffPosition, EmployeeStatus, EmployeeType, Gender
from university.models import EducationYear, Department



def employee_views(request):
    return render(request, 'pages/employee/employee-list.html')
def employee_list_json(request):
    hodimlar = CustomUser.objects.filter(user_type=2)

    # Prepare JSON data
    data = []
    for hodim in hodimlar:
        hodim_data = {
            'id': hodim.id,
            'image': hodim.imageFile.url if hodim.imageFile else (hodim.image if hodim.image else None),
            'full_name': hodim.full_name,
            'phone_number': hodim.phone_number,
            'email': hodim.email,
            'department': hodim.department.name if hodim.department else None,
            'user_type': hodim.staffPosition.name if hodim.staffPosition else None,
            'status': "Active" if hodim.is_active else "Inactive",
            'join_date': hodim.created_at.strftime('%Y-%m-%d'),
            # Add other fields as needed
        }
        data.append(hodim_data)

    # Return JSON response
    return JsonResponse(data, safe=False)


def create_employee_view(request):
    return render(request, 'pages/employee/create-employee.html')

def update_or_create(model, filter_kwargs, defaults=None):
    obj, created = model.objects.get_or_create(**filter_kwargs, defaults=defaults)
    if not created and defaults:
        for key, value in defaults.items():
            setattr(obj, key, value)
        obj.save()
    return obj, created

def create_employee_from_api(request):
    # cURL so'rovi uchun URL
    url = 'https://student.namspi.uz/rest/v1/data/employee-list?type=all'

    # cURL so'rovi uchun headers
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer cbdfefbb283db3a219a7e7dcefd620b4'
    }

    # cURL so'rovi uchun parametrlar
    employee_id_number = request.POST.get('employee_id_number')
    params = {
        'search': employee_id_number
    }
    try:
        # Ma'lumotlarni olish
        response = requests.get(url, headers=headers, params=params)
        # JSON javoblarni tekshirish
        if response.status_code == 200:

            data = response.json()
            for item in data.get('data', {}).get('items', []):
                staffPosition_name = item.get('staffPosition', {}).get('name')
                staffPosition_code = item.get('staffPosition', {}).get('code')
                defaults = {'code': staffPosition_code}
                obj, created = update_or_create(
                    StaffPosition,
                    filter_kwargs={'name': staffPosition_name},
                    defaults=defaults
                )
            for item in data.get('data', {}).get('items', []):
                employeeStatus_name = item.get('employeeStatus', {}).get('name')
                employeeStatus_code = item.get('employeeStatus', {}).get('code')
                defaults = {'code': employeeStatus_code}
                obj, created = update_or_create(
                    EmployeeStatus,
                    filter_kwargs={'name': employeeStatus_name},
                    defaults=defaults
                )

            for item in data.get('data', {}).get('items', []):
                employeeType_name = item.get('employeeType', {}).get('name')
                employeeType_code = item.get('employeeType', {}).get('code')
                defaults = {'code': employeeType_code}
                obj, created = update_or_create(
                    EmployeeType,
                    filter_kwargs={'name': employeeType_name},
                    defaults=defaults
                )
            if 'data' in data:
                item = data['data']['items'][0]

                # Ta'lim turi ni aniqlash
                employeeStatus_code = item.get('employeeStatus', {}).get('code')
                employeeStatus, _ = EmployeeStatus.objects.get_or_create(code=employeeStatus_code)

                # Ta'lim turi ni aniqlash
                employeeType_code = item.get('employeeType', {}).get('code')
                employeeType, _ = EmployeeType.objects.get_or_create(code=employeeType_code)

                # Ta'lim turi ni aniqlash
                StaffPosition_code = item.get('staffPosition', {}).get('code')
                staffPosition, _ = StaffPosition.objects.get_or_create(code=StaffPosition_code)

                # # Jinsini aniqlash
                gender_code = item.get('gender', {}).get('code')
                gender, _ = Gender.objects.get_or_create(code=gender_code)

                # Ta'lim turi ni aniqlash
                department_id = item.get('department', {}).get('id')
                department, _ = Department.objects.get_or_create(codeID=department_id)

                contract_date_timestamp = item.get('contract_date')
                contract_date = datetime.utcfromtimestamp(contract_date_timestamp)

                # created_at
                created_at_timestamp = item.get('created_at')
                created_at = datetime.utcfromtimestamp(created_at_timestamp)

                # updated_at
                updated_at_timestamp = item.get('updated_at')
                updated_at = datetime.utcfromtimestamp(updated_at_timestamp)

                # Rasmni URL sifatida saqlash
                image_url = item.get('image')



                # Ma'lumotlarni yangilash yoki yangi foydalanuvchi yaratish
                existing_user = CustomUser.objects.filter(employee_id_number=employee_id_number).first()
                if existing_user:
                    # Faydalanuvchi malumotlarini yangilash
                    existing_user.full_name = item.get('full_name', '')
                    existing_user.short_name = item.get('short_name', '')
                    existing_user.first_name = item.get('first_name', '')
                    existing_user.second_name = item.get('second_name', '')
                    existing_user.third_name = item.get('third_name', '')
                    existing_user.employee_id_number = item.get('employee_id_number', '')
                    existing_user.full_id = item.get('employee_id_number', '')
                    existing_user.image = image_url
                    existing_user.gender = gender
                    existing_user.employeeStatus = employeeStatus
                    existing_user.employeeType = employeeType
                    existing_user.staffPosition = staffPosition
                    existing_user.department = department
                    existing_user.contractDate = contract_date
                    existing_user.created_at = created_at
                    existing_user.updated_at = updated_at
                    existing_user.hash = item.get('hash', '')
                    existing_user.user_type = 2
                    existing_user.is_student = False
                    existing_user.is_active = True
                    existing_user.save()

                    return JsonResponse({'success': True, 'message': 'Foydalanuvchi ma\'lumotlari yangilandi'},
                                        status=200)
                else:
                    # Yangi foydalanuvchi yaratish
                    user, created = CustomUser.objects.get_or_create(
                        username=(item.get('first_name', '') + '_' + item.get('second_name', '') + str(
                            item.get('id', ''))).lower(),
                        email=(item.get('employee_id_number', '') + '@namdpi.uz').lower(),
                        defaults={
                            'full_name': item.get('full_name', ''),
                            'short_name': item.get('short_name', ''),
                            'first_name': item.get('first_name', ''),
                            'second_name': item.get('second_name', ''),
                            'third_name': item.get('third_name', ''),
                            'employee_id_number': item.get('employee_id_number', ''),
                            'full_id': item.get('employee_id_number', ''),
                            'image': image_url,
                            'employeeStatus': employeeStatus,
                            'employeeType': employeeType,
                            'staffPosition': staffPosition,
                            'password_save': (str(item.get('employee_id_number', '')) + 'namdpi'),
                            'department': department,
                            'contractDate': contract_date,
                            'created_at': created_at,
                            'updated_at': updated_at,
                            'hash': item.get('hash', ''),
                            'user_type': 2,
                            'is_student': False,
                            'is_active': True,
                        }
                    )

                # Agar yangi foydalanuvchi yaratilsa, parolni yaratish va saqlash
                if created:
                    # Parolni yaratish
                    password = make_password(str(item.get('employee_id_number')) + 'namdpi')
                    user.set_password(password)
                    user.save()

                    user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))
                    if user is not None:
                        # Foydalanuvchi avtorizatsiyadan o'tkazib, tizimga kirish
                        login(request, user)
                        # Agar muvaffaqiyatli bo'lsa, muvaffaqiyatli xabar qaytarish
                return JsonResponse({'success': True, 'message': 'Ma\'lumotlar muvaffaqiyatli saqlandi'}, status=201)
            else:
                return JsonResponse({'success': False, 'message': 'Ma\'lumotlar topilmadi'}, status=404)
        else:
            return JsonResponse({'success': False, 'message': 'Ma\'lumotlar olishda xatolik'}, status=500)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)



def get_employee_info(request):
    # Foydalanuvchi kiritish
    employee_id_number = request.GET.get('employee_id_number')

    # API so'rovni tayyorlash
    url = f'https://student.namspi.uz/rest/v1/data/employee-list?type=all&search={employee_id_number}'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer cbdfefbb283db3a219a7e7dcefd620b4'
    }

    # API ga so'rov tashlash
    response = requests.get(url, headers=headers)

    # Agar so'rov muvaffaqiyatli bo'lsa, javobni qaytarish
    if response.status_code == 200:
        employee_info = response.json()
        if CustomUser.objects.filter(employee_id_number=employee_id_number).exists():
            return JsonResponse(employee_info, status=200)
        return JsonResponse(employee_info, status=201)
    else:
        # Agar so'rov muvaffaqiyatsiz bo'lsa, xatolarni qaytarish
        return JsonResponse({'error': 'Foydalanuvchi malumotlarini olishda xatolik yuz berdi'}, status=500)