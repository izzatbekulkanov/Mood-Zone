from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import JsonResponse

from .models import Library, AdminLibrary, Book


@login_required
def create_library_json(request):
    if request.method == 'POST':
        # Foydalanuvchi obyektini olish
        user = request.user

        # POST so'rov orqali kutubhona ma'lumotlarini olish
        name = request.POST.get('name')
        address = request.POST.get('address')
        number = request.POST.get('number')
        status = request.POST.get('status')

        # Boolean qiymatga o'tkazish
        if status == 'true':
            status = True
        else:
            status = False

        # Yangi kutubhona obyektini yaratish
        new_library = Library(name=name, address=address, number=number, user=user, active=status)
        new_library.save()

        # Kutubhonani muvaffaqiyatli yaratilgandan keyin foydalanuvchini profiliga yo'naltirish
        return JsonResponse({'success': True, 'message': 'Kutubhona muvaffaqiyatli saqlandi'}, status=200)

    # Agar POST so'rov emas bo'lsa yoki AJAX emas bo'lsa, xatolik qaytarish
    return JsonResponse({'success': False, 'message': 'Kutubhona yaratishda hatolik bor'}, status=404)


def libraries_list(request):
    # Barcha kutubhonalar ro'yxati
    libraries = Library.objects.all().order_by('-id')
    admin_libraries = AdminLibrary.objects.filter(is_deleted=False)

    # Ma'lumotlar to'plamini saqlash uchun bo'sh ro'yxat
    data = []

    # Har bir kutubhonani o'qib ko'rish
    for library in libraries:
        # Kutubhonaga birikkan foydalanuvchi borligini tekshirish
        admin_library = admin_libraries.filter(library=library).first()

        if admin_library:
            # Kutubhona ma'lumotlari

            library_data = {
                'id': library.id,
                'name': library.name,
                'address': library.address,
                # Kutubhonaga birikkan foydalanuvchi ma'lumotlari
                'admin': {
                    'username': admin_library.user.username,
                    'full_name': admin_library.user.full_name,
                    # Boshqa foydalanuvchi ma'lumotlarini ham qo'shishingiz mumkin
                    # 'email': admin_library.user.email,
                    # ...
                },
                'adminLibraryId': admin_library.id
            }
        else:
            # Agar kutubhonaga foydalanuvchi birikmagan bo'lsa
            library_data = {
                'id': library.id,
                'name': library.name,
                'address': library.address,
                'admin': None
            }

        # Ma'lumotlarni to'plamga qo'shish
        data.append(library_data)

    # JSON ko'rinishida ma'lumotlarni qaytarish
    return JsonResponse(data, safe=False)


def get_library_users(request):
    # Library groupni olish
    try:
        library_group = Group.objects.get(name='Library')
    except Group.DoesNotExist:
        return JsonResponse({'error': 'Library group not found'}, status=404)

    # Library groupga tegishli foydalanuvchilarni olish
    library_users = library_group.user_set.all()

    # Foydalanuvchilarni JSON formatida qaytarish
    users_data = []
    for user in library_users:
        users_data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'third_name': user.third_name,
            'full_name': user.full_name,

            # Boshqa foydalanuvchi maydonlari kerak bo'lsa, ularni ham qo'shing
        })

    return JsonResponse({'users': users_data})


def add_librarian(request):
    if request.method == 'POST':
        librarian_id = request.POST.get('librarian_id')
        library_id = request.POST.get('library_id')

        try:
            # Kutubxona uchun foydalanuvchi borligini va is_deleted holatini tekshirish
            existing_admin_library = AdminLibrary.objects.filter(library_id=library_id).first()
            existing_admin_librarian = AdminLibrary.objects.filter(user_id=librarian_id).last()

            # Shartni qo'shish
            if existing_admin_library is None or not existing_admin_library.is_deleted == False:
                # Kutubxona uchun foydalanuvchi yo'q, yoki is_deleted=False
                admin_library = AdminLibrary.objects.create(
                    user_id=librarian_id,
                    library_id=library_id,
                    is_active=True,
                    is_deleted=False
                )
                # Kutubxona uchun foydalanuvchi bor va is_deleted=False
                return JsonResponse({'success': True, 'message': 'Librarian added successfully'}, status=200)

            else:
                return JsonResponse({'success': False, 'message': 'Library already has a librarian or is deleted'},status=400)
        except Exception as e:
            # Xatolik xabari
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    else:
        # Not allowed metod xatoligi
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def soft_delete_admin_library(request, admin_library_id):
    try:
        admin_library = AdminLibrary.objects.get(id=admin_library_id)
        admin_library.is_deleted = True
        admin_library.is_active = False
        admin_library.save()
        return JsonResponse({'success': True, 'message': 'Admin library soft deleted successfully'})
    except AdminLibrary.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Admin library not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


def send_library_group_users(request):
    try:
        # "Library" nomli guruhni olish
        library_group = Group.objects.get(name='Library')

        # Guruh a'zolari
        users = library_group.user_set.all()
        user_data = []

        # Foydalanuvchilarni olish va tekshirish
        for user in users:
            # Foydalanuvchi uchun "AdminLibrary" obyektini olish
            admin_library = AdminLibrary.objects.filter(user=user).first()

            # Agar foydalanuvchining AdminLibrary obyekti mavjud bo'lsa va is_deleted=False bo'lsa
            if admin_library and not admin_library.is_deleted:
                # Kutubhona nomi va raqami
                library_name = admin_library.library.name
                library_code = admin_library.library.number

                # Kutubhonaga biriktirilgan kitoblar sonini hisoblash
                book_count = Book.objects.filter(library=admin_library.library).count()

                user_info = {
                    'username': user.username,
                    'full_name': user.get_full_name(),
                    'email': user.email,
                    'library_name': library_name,  # Kutubhona nomini qo'shish
                    'library_number': library_code,  # Kutubhona raqamini qo'shish
                    'book_count': book_count,  # Kutubhona biriktirilgan kitoblar soni
                    # Qo'shimcha ma'lumotlar
                }
                user_data.append(user_info)

        # JSON ko'rinishida foydalanuvchilar ro'yxatini qaytarish
        return JsonResponse(user_data, safe=False)

    except Group.DoesNotExist:
        # Agar guruh mavjud bo'lmasa
        return JsonResponse({'error': 'Library group does not exist'}, status=404)