from datetime import datetime

import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.http import JsonResponse

from account.models import CustomUser, Accommodation, StudentType, PaymentForm, StudentStatus, Citizenship, District, \
    Province, Country, Gender
from university.models import EducationYear, Semester, Level, GroupUniver, Specialty, Curriculum, Department, \
    EducationType, EducationForm, University


def create_follower_from_api(request):
    # cURL so'rovi uchun URL
    url = 'https://student.namdu.uz/rest/v1/data/student-info'
    # cURL so'rovi uchun headers
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer cbdfefbb283db3a219a7e7dcefd620b4'
    }

    def update_or_create(model, filter_kwargs, defaults=None):
        obj, created = model.objects.get_or_create(**filter_kwargs, defaults=defaults)
        if not created and defaults:
            for key, value in defaults.items():
                setattr(obj, key, value)
            obj.save()
        return obj, created


    # cURL so'rovi uchun parametrlar
    student_id_number = request.POST.get('student_id_number')
    params = {
        'student_id_number': student_id_number
    }

    # 'EducationForm' modelini o'zgartirish


    try:
        # Ma'lumotlarni olish
        response = requests.get(url, headers=headers, params=params)
        # JSON javoblarni tekshirish
        if response.status_code == 200:
            data = response.json()

            if 'data' in data:
                item = data['data']

                # Ta'lim turi ni aniqlash
                university_code = item.get('university', {}).get('code')
                university, _ = University.objects.get_or_create(code=university_code)
                print(university)
                # Jinsi
                gender_code = item.get('gender', {}).get('code')
                gender, _ = Gender.objects.get_or_create(code=gender_code)
                print(gender)

                # Mamlakat
                country_code = item.get('country', {}).get('code')
                country, _ = Country.objects.get_or_create(code=country_code)
                print(country)

                # Viloyatni aniqlash
                province_code = item.get('province', {}).get('code')
                province, _ = Province.objects.get_or_create(code=province_code)
                print("province")

                # Tumanni aniqlash
                district_code = item.get('district', {}).get('code')
                district, _ = District.objects.get_or_create(code=district_code)
                print("district")

                # Ta'lim turi ni aniqlash
                citizenship_code = item.get('citizenship', {}).get('code')
                citizenship, _ = Citizenship.objects.get_or_create(code=citizenship_code)
                print("citizenship")

                # Ta'lim turi ni aniqlash
                studentStatus_code = item.get('studentStatus', {}).get('code')
                studentStatus, _ = StudentStatus.objects.get_or_create(code=studentStatus_code)
                print("studentStatus")

                # Ta'lim turi ni aniqlash
                educationForm_code = item.get('educationForm', {}).get('code')
                educationForm, _ = EducationForm.objects.get_or_create(code=educationForm_code)
                print("educationForm")

                # Ta'lim turi ni aniqlash
                educationType_code = item.get('educationType', {}).get('code')
                educationType, _ = EducationType.objects.get_or_create(code=educationType_code)
                print("educationType")

                # Ta'lim turi ni aniqlash
                paymentForm_code = item.get('paymentForm', {}).get('code')
                paymentForm, _ = PaymentForm.objects.get_or_create(code=paymentForm_code)
                print("paymentForm")

                # Ta'lim turi ni aniqlash
                studentType_code = item.get('studentType', {}).get('code')
                studentType, _ = StudentType.objects.get_or_create(code=studentType_code)
                print("studentType")

                # Ta'lim turi ni aniqlash
                accommodation_code = item.get('accommodation', {}).get('code')
                accommodation, _ = Accommodation.objects.get_or_create(code=accommodation_code)
                print("accommodation")

                # Ta'lim turi ni aniqlash
                department_id = item.get('department', {}).get('id')
                department, _ = Department.objects.get_or_create(codeID=department_id)
                print("department")

                # # O'quv rejani aniqlash'
                curriculum_code = item.get('department', {}).get('id')
                curriculum, _ = Curriculum.objects.get_or_create(codeID=curriculum_code)
                print("curriculum")

                # # Ta'lim turi ni aniqlash
                # specialty_code = item.get('specialty', {}).get('id')
                # print(specialty_code)
                # print(Specialty.objects.get_or_create(codeID=specialty_code))
                # specialty, _ = Specialty.objects.get_or_create(codeID=specialty_code)
                # print("specialty")

                # Ta'lim turi ni aniqlash
                group_id = item.get('group', {}).get('id')
                group, _ = GroupUniver.objects.get_or_create(codeID=group_id)
                print("group")

                # Ta'lim turi ni aniqlash
                level_code = item.get('level', {}).get('code')
                level, _ = Level.objects.get_or_create(code=level_code)
                print("Level")

                # Ta'lim turi ni aniqlash
                semester_code = item.get('semester', {}).get('code')
                semester, _ = Semester.objects.get_or_create(code=semester_code)
                print("Semenstr")

                # Ta'lim turi ni aniqlash
                educationYear_code = item.get('educationYear', {}).get('code')
                educationYear, _ = EducationYear.objects.get_or_create(code=educationYear_code)
                print("Education year")

                birth_date_timestamp = item.get('birth_date')
                birth_date = datetime.utcfromtimestamp(birth_date_timestamp)
                print("Tugilgan kuni")

                # created_at
                created_at_timestamp = item.get('created_at')
                created_at = datetime.utcfromtimestamp(created_at_timestamp)
                print("Yaratilgan sana")

                # updated_at
                updated_at_timestamp = item.get('updated_at')
                updated_at = datetime.utcfromtimestamp(updated_at_timestamp)
                print("Yangilangan sana")
                # Rasmni URL sifatida saqlash

                image_url = item.get('image')

                # Rasmni yuklab olish va rasm faylini saqlash
                # if image_url:
                #     img_temp = NamedTemporaryFile(delete=True)
                #     img_temp.write(urllib.request.urlopen(image_url).read())
                #     img_temp.flush()
                #     img_temp.close()

                user, created = CustomUser.objects.get_or_create(
                    username=(item.get('first_name') + '_' + item.get('second_name') + str(item.get('id'))).lower(),
                    email=(item.get('first_name') + '_' + item.get('second_name') + str(
                        item.get('id')) + '@namdpi.uz').lower(),
                    defaults={
                        'university': university,
                        'full_name': item.get('full_name'),
                        'short_name': item.get('short_name'),
                        'first_name': item.get('first_name'),
                        'second_name': item.get('second_name'),
                        'third_name': item.get('third_name'),
                        'gender': gender,
                        'birth_date': birth_date,
                        'student_id_number': item.get('student_id_number'),
                        'full_id': item.get('student_id_number'),
                        'image': image_url,
                        # 'imageFile': File(open(img_temp.name, 'rb')),
                        'country': country,
                        'province': province,
                        'district': district,
                        'citizenship': citizenship,
                        'studentStatus': studentStatus,
                        'educationForm': educationForm,
                        'educationType': educationType,
                        'password_save': (str(item.get('student_id_number')) + 'namdpi'),
                        'paymentForm': paymentForm,
                        'studentType': studentType,
                        'accommodation': accommodation,
                        'department': department,
                        'curriculum': curriculum,
                        # 'specialty': specialty,
                        'group': group,
                        'level': level,
                        'semester': semester,
                        'educationYear': educationYear,
                        'year_of_enter': item.get('year_of_enter'),
                        'created_at': created_at,
                        'updated_at': updated_at,
                        'hash': item.get('hash'),
                        'user_type': 1,
                        'is_student': True,
                        'is_followers_book': True,
                        'now_role': 'Student',
                        'is_active': True,  # Active holatda
                    }
                )

                # Agar yangi foydalanuvchi yaratilsa, parolni yaratish va saqlash
                if created:
                    # Parolni yaratish
                    password = make_password(str(item.get('student_id_number')) + 'namdpi')
                    user.set_password(password)
                    student_group = Group.objects.get(name='Student')
                    user.now_role = 'Student'
                    user.groups.add(student_group)
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

