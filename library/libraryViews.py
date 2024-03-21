from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Library, AdminLibrary


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
    admin_libraries = AdminLibrary.objects.all()

    # Ma'lumotlar to'plamini saqlash uchun bo'sh ro'yxat
    data = []

    # Har bir kutubhonani o'qib ko'rish
    for library in libraries:
        # Kutubhonaga birikkan foydalanuvchi borligini tekshirish
        admin_library = admin_libraries.filter(library=library).first()

        if admin_library:
            # Kutubhona ma'lumotlari
            library_data = {
                'name': library.name,
                'address': library.address,
                # Kutubhonaga birikkan foydalanuvchi ma'lumotlari
                'admin': {
                    'username': admin_library.user.username,
                    'full_name': admin_library.user.full_name,
                    # Boshqa foydalanuvchi ma'lumotlarini ham qo'shishingiz mumkin
                    # 'email': admin_library.user.email,
                    # ...
                }
            }
        else:
            # Agar kutubhonaga foydalanuvchi birikmagan bo'lsa
            library_data = {
                'name': library.name,
                'address': library.address,
                'admin': None
            }

        # Ma'lumotlarni to'plamga qo'shish
        data.append(library_data)

    # JSON ko'rinishida ma'lumotlarni qaytarish
    return JsonResponse(data, safe=False)
