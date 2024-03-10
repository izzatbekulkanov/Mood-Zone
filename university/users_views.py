from datetime import datetime

import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

from account.models import CustomUser, Gender, Country, Province, District, Citizenship, StudentStatus, PaymentForm, \
    StudentType, Accommodation
from university.models import Department, Specialty, Level, Semester, EducationYear, University, EducationForm, \
    EducationType, GroupUniver, Curriculum


def save_student_from_api(request):
    url = 'https://student.namspi.uz/rest/v1/data/student-list?page=30&limit=100'
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

    try:

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Agar status kod 200 bo'lmasa, xato qaytaradi
        data = response.json()
        # if data:
        #     return JsonResponse({'success': True, 'message': data}, status=201)

        for item in data.get('data', {}).get('items', []):
            gender_name = item.get('gender', {}).get('name')
            gender_code = item.get('gender', {}).get('code')
            defaults = {'code': gender_code}
            obj, created = update_or_create(
                Gender,
                filter_kwargs={'name': gender_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            country_name = item.get('country', {}).get('name')
            country_code = item.get('country', {}).get('code')
            defaults = {'code': country_code}
            obj, created = update_or_create(
                Country,
                filter_kwargs={'name': country_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            province_name = item.get('province', {}).get('name')
            province_code = item.get('province', {}).get('code')
            defaults = {'code': province_code}
            obj, created = update_or_create(
                Province,
                filter_kwargs={'name': province_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            district_name = item.get('district', {}).get('name')
            district_code = item.get('district', {}).get('code')
            defaults = {'code': district_code}
            obj, created = update_or_create(
                District,
                filter_kwargs={'name': district_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            citizenship_name = item.get('citizenship', {}).get('name')
            citizenship_code = item.get('citizenship', {}).get('code')
            defaults = {'code': citizenship_code}
            obj, created = update_or_create(
                Citizenship,
                filter_kwargs={'name': citizenship_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            studentStatus_name = item.get('studentStatus', {}).get('name')
            studentStatus_code = item.get('studentStatus', {}).get('code')
            defaults = {'code': studentStatus_code}
            obj, created = update_or_create(
                StudentStatus,
                filter_kwargs={'name': studentStatus_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            studentType_name = item.get('studentType', {}).get('name')
            studentType_code = item.get('studentType', {}).get('code')
            defaults = {'code': studentType_code}
            obj, created = update_or_create(
                StudentType,
                filter_kwargs={'name': studentType_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            paymentForm_name = item.get('paymentForm', {}).get('name')
            paymentForm_code = item.get('paymentForm', {}).get('code')
            defaults = {'code': paymentForm_code}
            obj, created = update_or_create(
                PaymentForm,
                filter_kwargs={'name': paymentForm_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            accommodation_name = item.get('accommodation', {}).get('name')
            accommodation_code = item.get('accommodation', {}).get('code')
            defaults = {'code': accommodation_code}
            obj, created = update_or_create(
                Accommodation,
                filter_kwargs={'name': accommodation_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            level_name = item.get('level', {}).get('name')
            level_code = item.get('level', {}).get('code')
            defaults = {'code': level_code}
            obj, created = update_or_create(
                Level,
                filter_kwargs={'name': level_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            semester_name = item.get('semester', {}).get('name')
            semester_code = item.get('semester', {}).get('code')
            defaults = {'code': semester_code}
            obj, created = update_or_create(
                Semester,
                filter_kwargs={'name': semester_name},
                defaults=defaults
            )
        for item in data.get('data', {}).get('items', []):
            educationYear_name = item.get('educationYear', {}).get('name')
            educationYear_code = item.get('educationYear', {}).get('code')
            defaults = {'code': educationYear_code}
            obj, created = update_or_create(
                EducationYear,
                filter_kwargs={'name': educationYear_name},
                defaults=defaults
            )

        # API-dan olingan ma'lumotlarni CustomUser modeliga saqlash
        for item in data.get('data', {}).get('items', []):
            # Ta'lim turi ni aniqlash
            university_code = item.get('university', {}).get('code')
            university, _ = University.objects.get_or_create(code=university_code)
            # Jinsi
            gender_code = item.get('gender', {}).get('code')
            gender, _ = Gender.objects.get_or_create(code=gender_code)
            # Mamlakat
            country_code = item.get('country', {}).get('code')
            country, _ = Country.objects.get_or_create(code=country_code)

            # Viloyatni aniqlash
            province_code = item.get('province', {}).get('code')
            province, _ = Province.objects.get_or_create(code=province_code)

            # Tumanni aniqlash
            district_code = item.get('district', {}).get('code')
            district, _ = District.objects.get_or_create(code=district_code)

            # Ta'lim turi ni aniqlash
            citizenship_code = item.get('citizenship', {}).get('code')
            citizenship, _ = Citizenship.objects.get_or_create(code=citizenship_code)

            # Ta'lim turi ni aniqlash
            studentStatus_code = item.get('studentStatus', {}).get('code')
            studentStatus, _ = StudentStatus.objects.get_or_create(code=studentStatus_code)

            # Ta'lim turi ni aniqlash
            educationForm_code = item.get('educationForm', {}).get('code')
            educationForm, _ = EducationForm.objects.get_or_create(code=educationForm_code)

            # Ta'lim turi ni aniqlash
            educationType_code = item.get('educationType', {}).get('code')
            educationType, _ = EducationType.objects.get_or_create(code=educationType_code)

            # Ta'lim turi ni aniqlash
            paymentForm_code = item.get('paymentForm', {}).get('code')
            paymentForm, _ = PaymentForm.objects.get_or_create(code=paymentForm_code)

            # Ta'lim turi ni aniqlash
            studentType_code = item.get('studentType', {}).get('code')
            studentType, _ = StudentType.objects.get_or_create(code=studentType_code)

            # Ta'lim turi ni aniqlash
            accommodation_code = item.get('accommodation', {}).get('code')
            accommodation, _ = Accommodation.objects.get_or_create(code=accommodation_code)

            # Ta'lim turi ni aniqlash
            department_id = item.get('department', {}).get('id')
            department, _ = Department.objects.get_or_create(codeID=department_id)

            # Ta'lim turi ni aniqlash
            specialty_id = item.get('specialty', {}).get('id')
            specialty, _ = Specialty.objects.get_or_create(codeID=specialty_id)

            # Ta'lim turi ni aniqlash
            group_id = item.get('group', {}).get('id')
            group, _ = GroupUniver.objects.get_or_create(codeID=group_id)

            # Ta'lim turi ni aniqlash
            level_code = item.get('level', {}).get('code')
            level, _ = Level.objects.get_or_create(code=level_code)

            # Ta'lim turi ni aniqlash
            semester_code = item.get('semester', {}).get('code')
            semester, _ = Semester.objects.get_or_create(code=semester_code)

            # Ta'lim turi ni aniqlash
            educationYear_code = item.get('educationYear', {}).get('code')
            educationYear, _ = EducationYear.objects.get_or_create(code=educationYear_code)

            birth_date_timestamp = item.get('birth_date')
            birth_date = datetime.utcfromtimestamp(birth_date_timestamp)

            # created_at
            created_at_timestamp = item.get('created_at')
            created_at = datetime.utcfromtimestamp(created_at_timestamp)

            # updated_at
            updated_at_timestamp = item.get('updated_at')
            updated_at = datetime.utcfromtimestamp(updated_at_timestamp)

            # Speciality obyektini yaratish va saqlash
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
                    'image': item.get('image'),
                    'country': country,
                    'province': province,
                    'district': district,
                    'citizenship': citizenship,
                    'studentStatus': studentStatus,
                    'educationForm': educationForm,
                    'educationType': educationType,
                    'paymentForm': paymentForm,
                    'studentType': studentType,
                    'accommodation': accommodation,
                    'department': department,
                    'specialty': specialty,
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
                    'user_role': 'student',
                    'is_active': True,  # Active holatda
                }
            )

            # Agar yangi foydalanuvchi yaratilsa, parolni yaratish va saqlash
            if created:
                password = make_password(str(item.get('id')))  # Parolni yaratish
                user.password_save = password
                user.save()

        return JsonResponse({'success': True, 'message': 'Ma\'lumotlar muvaffaqiyatli saqlandi'}, status=201)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


def create_student_from_api(request):
    # cURL so'rovi uchun URL
    url = 'https://student.namspi.uz/rest/v1/data/student-info'
    # cURL so'rovi uchun headers
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer cbdfefbb283db3a219a7e7dcefd620b4'
    }
    # cURL so'rovi uchun parametrlar
    student_id_number = request.POST.get('student_id_number')
    print(student_id_number)
    params = {
        'student_id_number': student_id_number
    }

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
                # Jinsi
                gender_code = item.get('gender', {}).get('code')
                gender, _ = Gender.objects.get_or_create(code=gender_code)
                print("Shu Jinsi")

                # Mamlakat
                country_code = item.get('country', {}).get('code')
                country, _ = Country.objects.get_or_create(code=country_code)
                print("Shu Mamlakat")

                # Viloyatni aniqlash
                province_code = item.get('province', {}).get('code')
                province, _ = Province.objects.get_or_create(code=province_code)
                print("Shu provinse")

                # Tumanni aniqlash
                district_code = item.get('district', {}).get('code')
                district, _ = District.objects.get_or_create(code=district_code)
                print("Shu kocha")

                # Ta'lim turi ni aniqlash
                citizenship_code = item.get('citizenship', {}).get('code')
                citizenship, _ = Citizenship.objects.get_or_create(code=citizenship_code)
                print("Shu Sitizen")

                # Ta'lim turi ni aniqlash
                studentStatus_code = item.get('studentStatus', {}).get('code')
                studentStatus, _ = StudentStatus.objects.get_or_create(code=studentStatus_code)
                print("Shu Status")

                # Ta'lim turi ni aniqlash
                educationForm_code = item.get('educationForm', {}).get('code')
                educationForm, _ = EducationForm.objects.get_or_create(code=educationForm_code)
                print("Shu Education form")

                # Ta'lim turi ni aniqlash
                educationType_code = item.get('educationType', {}).get('code')
                educationType, _ = EducationType.objects.get_or_create(code=educationType_code)
                print("Shu Education Type")

                # Ta'lim turi ni aniqlash
                paymentForm_code = item.get('paymentForm', {}).get('code')
                paymentForm, _ = PaymentForm.objects.get_or_create(code=paymentForm_code)
                print("Shu Payment Form")

                # Ta'lim turi ni aniqlash
                studentType_code = item.get('studentType', {}).get('code')
                studentType, _ = StudentType.objects.get_or_create(code=studentType_code)
                print("Shu Student Type")

                # Ta'lim turi ni aniqlash
                accommodation_code = item.get('accommodation', {}).get('code')
                accommodation, _ = Accommodation.objects.get_or_create(code=accommodation_code)
                print("Shu Accomidation")

                # Ta'lim turi ni aniqlash
                department_id = item.get('department', {}).get('id')
                department, _ = Department.objects.get_or_create(codeID=department_id)
                print("Shu Department")

                # # O'quv rejani aniqlash'
                curriculum_code = item.get('department', {}).get('id')
                curriculum, _ = Curriculum.objects.get_or_create(codeID=curriculum_code)
                print("Shu Curriculum")

                # Ta'lim turi ni aniqlash
                specialty_code = item.get('specialty', {}).get('code')
                specialty, _ = Specialty.objects.get_or_create(code=specialty_code)
                print("Shu Specialty")

                # Ta'lim turi ni aniqlash
                group_id = item.get('group', {}).get('id')
                group, _ = GroupUniver.objects.get_or_create(codeID=group_id)
                print("Shu Group")

                # Ta'lim turi ni aniqlash
                level_code = item.get('level', {}).get('code')
                level, _ = Level.objects.get_or_create(code=level_code)
                print("Shu Level")

                # Ta'lim turi ni aniqlash
                semester_code = item.get('semester', {}).get('code')
                semester, _ = Semester.objects.get_or_create(code=semester_code)
                print("Shu Semenstr")

                # Ta'lim turi ni aniqlash
                educationYear_code = item.get('educationYear', {}).get('code')
                educationYear, _ = EducationYear.objects.get_or_create(code=educationYear_code)
                print("Shu Education year")

                birth_date_timestamp = item.get('birth_date')
                birth_date = datetime.utcfromtimestamp(birth_date_timestamp)
                print("Shu Tugilgan kuni")

                # created_at
                created_at_timestamp = item.get('created_at')
                created_at = datetime.utcfromtimestamp(created_at_timestamp)
                print("Shu Yaratilgan sana")

                # updated_at
                updated_at_timestamp = item.get('updated_at')
                updated_at = datetime.utcfromtimestamp(updated_at_timestamp)
                print("Shu Yangilangan sana")
                # Rasmni URL sifatida saqlash

                image_url = item.get('image')

                # Rasmni yuklab olish va rasm faylini saqlash
                # if image_url:
                #     img_temp = NamedTemporaryFile(delete=True)
                #     img_temp.write(urllib.request.urlopen(image_url).read())
                #     img_temp.flush()
                #     img_temp.close()

                # Speciality obyektini yaratish va saqlash
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
                        'specialty': specialty,
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
                        'user_role': 'student',
                        'is_active': True,  # Active holatda
                    }
                )

                # Agar yangi foydalanuvchi yaratilsa, parolni yaratish va saqlash
                if created:
                    # Parolni yaratish
                    password = make_password(str(item.get('student_id_number')) + 'namdpi')
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


def get_student_info(request):
    # Foydalanuvchi kiritish
    student_id_number = request.GET.get('student_id_number')

    # API so'rovni tayyorlash
    url = f'https://student.namspi.uz/rest/v1/data/student-info?student_id_number={student_id_number}'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer cbdfefbb283db3a219a7e7dcefd620b4'
    }

    # API ga so'rov tashlash
    response = requests.get(url, headers=headers)

    # Agar so'rov muvaffaqiyatli bo'lsa, javobni qaytarish
    if response.status_code == 200:
        student_info = response.json()
        if CustomUser.objects.filter(student_id_number=student_id_number).exists():
            return JsonResponse(student_info, status=200)
        return JsonResponse(student_info, status=201)
    else:
        # Agar so'rov muvaffaqiyatsiz bo'lsa, xatolarni qaytarish
        return JsonResponse({'error': 'Foydalanuvchi malumotlarini olishda xatolik yuz berdi'}, status=500)
