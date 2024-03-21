import requests
from django.http import JsonResponse, HttpResponse

from university.models import University, EducationType, Specialty, Department, EducationForm, Curriculum, \
    EducationLang, GroupUniver
from university.serializers import UniversitySerializer, SpecialtySerializer, CurriculumSerializer, \
    GroupUniverSerializer


def update_or_create(model, filter_kwargs, defaults=None):
    obj, created = model.objects.get_or_create(**filter_kwargs, defaults=defaults)
    if not created and defaults:
        for key, value in defaults.items():
            setattr(obj, key, value)
        obj.save()
    return obj, created


def update_or_create_department(data):
    department_id = data.get('id')
    name = data.get('name')
    code = data.get('code')
    parent = data.get('parent', None)
    active = data.get('active', False)
    structure_type = data.get('structureType', {}).get('code')

    department, created = Department.objects.update_or_create(
        codeID=department_id,
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


def save_university_from_api(request):
    url = 'https://student.namspi.uz/rest/v1/public/university-list?page=20&limit=200'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer cbdfefbb283db3a219a7e7dcefd620b4'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        universities = data.get('data', [])
        for university_data in universities:
            code = university_data.get('code', '')
            name = university_data.get('name', '')
            api_url = university_data.get('api_url', '')
            student_url = university_data.get('student_url', '')
            employee_url = university_data.get('employee_url', '')

            # Check if the university already exists in the database
            existing_university = University.objects.filter(code=code).first()
            if existing_university:
                # Update the existing university
                existing_university.name = name
                existing_university.api_url = api_url
                existing_university.student_url = student_url
                existing_university.employee_url = employee_url
                existing_university.save()
            else:
                # Create a new university
                University.objects.create(
                    code=code,
                    name=name,
                    api_url=api_url,
                    student_url=student_url,
                    employee_url=employee_url
                )

        return HttpResponse("Successfully updated the university list.")
    else:
        return HttpResponse("Failed to update the university list. Status code: {}".format(response.status_code),
                            status=response.status_code)


def save_specialty_from_api(request):
    url = 'https://student.namspi.uz/rest/v1/data/specialty-list?page=20&limit=200'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer cbdfefbb283db3a219a7e7dcefd620b4'
    }

    try:

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Agar status kod 200 bo'lmasa, xato qaytaradi
        data = response.json()
        for item in data.get('data', {}).get('items', []):
            education_type_name = item.get('educationType', {}).get('name')
            education_type_code = item.get('educationType', {}).get('code')
            defaults = {'code': education_type_code}
            obj, created = update_or_create(
                EducationType,
                filter_kwargs={'name': education_type_name},
                defaults=defaults
            )

        # API-dan olingan ma'lumotlarni Speciality modeliga saqlash
        for item in data.get('data', {}).get('items', []):
            # Bo'limni aniqlash
            department_id = item.get('department', {}).get('id')
            department, _ = Department.objects.get_or_create(codeID=department_id)

            # Ta'lim turi ni aniqlash
            education_type_code = item.get('educationType', {}).get('code')
            education_type, _ = EducationType.objects.get_or_create(code=education_type_code)

            # Speciality obyektini yaratish va saqlash
            Specialty.objects.update_or_create(
                codeID=item.get('id'),
                defaults={
                    'code': item.get('code'),
                    'name': item.get('name'),
                    'department': department,
                    'educationType': education_type
                }
            )

        return JsonResponse({'success': True, 'message': 'Ma\'lumotlar muvaffaqiyatli saqlandi'}, status=201)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


def save_curriculum_from_api(request):
    url = 'https://student.namspi.uz/rest/v1/data/curriculum-list?page=20&limit=200'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer cbdfefbb283db3a219a7e7dcefd620b4'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Agar status kod 200 bo'lmasa, xato qaytaradi
        data = response.json()

        # 'EducationForm' modelini o'zgartirish
        for item in data.get('data', {}).get('items', []):
            education_form_name = item.get('educationForm', {}).get('name')
            education_form_code = item.get('educationForm', {}).get('code')
            EducationForm.objects.get_or_create(
                name=education_form_name,
                defaults={'code': education_form_code}
            )

        # 'Curriculum' obyektlarini saqlash
        for item in data.get('data', {}).get('items', []):
            specialty_id = item.get('specialty', {}).get('id')
            specialty, _ = Specialty.objects.get_or_create(codeID=specialty_id)

            education_type_code = item.get('educationType', {}).get('code')
            education_type, _ = EducationType.objects.get_or_create(code=education_type_code)

            education_form_code = item.get('educationForm', {}).get('code')
            education_form = EducationForm.objects.get(code=education_form_code)

            defaults = {
                'name': item.get('name'),
                'specialty': specialty,
                'educationType': education_type,
                'educationForm': education_form,
                'semester_count': item.get('semester_count'),
                'education_period': item.get('education_period'),
            }
            Curriculum.objects.update_or_create(
                codeID=item.get('id'),
                defaults=defaults
            )

        return JsonResponse({'success': True, 'message': 'Ma\'lumotlar muvaffaqiyatli saqlandi'}, status=201)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


def save_group_from_api(request):
    url = 'https://student.namspi.uz/rest/v1/data/group-list?limit=400'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer cbdfefbb283db3a219a7e7dcefd620b4'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        for item in data.get('data', {}).get('items', []):
            # Ta'lim turi ni aniqlash
            education_lang_code = item.get('educationLang', {}).get('code')
            education_lang, _ = EducationLang.objects.get_or_create(code=education_lang_code)

            # Fakultetni aniqlash
            department_code = item.get('department', {}).get('id')
            department, _ = Department.objects.get_or_create(codeID=department_code)

            # Yo'nalishni aniqlash
            specialty_id = item.get('specialty', {}).get('id')
            specialty, _ = Specialty.objects.get_or_create(codeID=specialty_id)

            # Ta'lim rejani aniqlash
            # curriculum_id = item.get('_curriculum')
            # curriculum, _ = Curriculum.objects.get_or_create(codeID=curriculum_id)

            # Guruh obyektini yaratish va saqlash
            GroupUniver.objects.update_or_create(
                codeID=item.get('id'),
                defaults={
                    'name': item.get('name'),
                    'educationLang': education_lang,
                    'department': department,
                    'specialty': specialty,
                    # 'curriculum': curriculum,
                }
            )

        return JsonResponse({'success': True, 'message': 'Ma\'lumotlar muvaffaqiyatli saqlandi'}, status=201)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


def get_universities_data(request):
    specialties = Specialty.objects.all()
    specialties_count = Specialty.objects.count()

    universities = University.objects.all()  # Universitetlar ro'yxati
    universities_count = universities.count()  # Universitetlar soni

    curriculums = Curriculum.objects.all()  # Universitetlar ro'yxati
    curriculums_count = curriculums.count()  # Universitetlar soni

    groups = GroupUniver.objects.all()  # Guruhlar ro'yxati
    groups_count = groups.count()  # Guruhlar soni

    serializer = UniversitySerializer(universities, many=True)  # Serializer
    specialtySerializer = SpecialtySerializer(specialties, many=True)  # Serializer
    curriculumSerializer = CurriculumSerializer(curriculums, many=True)  # Serializer
    groupSerializer = GroupUniverSerializer(groups, many=True)  # Serializer
    data = {'universities': serializer.data,
            'count': universities_count,
            'specialty': specialtySerializer.data,
            'specialty_count': specialties_count,
            'curriculums': curriculumSerializer.data,
            'curriculums_count': curriculums_count,
            'groups': groupSerializer.data,
            'groups_count': groups_count
            }  # Ma'lumotlar va son
    return JsonResponse(data, safe=False)  # JSON formatida javob


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
