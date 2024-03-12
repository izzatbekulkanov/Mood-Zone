from django.db.models import F
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from account.models import CustomUser
from library.models import Book, BookLoan


def get_user_by_student_id(request):
    if request.method == 'GET':
        # `student_user_id` ni request parametrlaridan olish
        student_user_id = request.GET.get('student_user_id')
        if not student_user_id:
            return JsonResponse({'success': False, 'message': 'Student user ID not provided'}, status=400)

        try:
            # Foydalanuvchini qidirish
            user = CustomUser.objects.get(student_id_number=student_user_id)
            # Foydalanuvchini JSON shaklida qaytarish
            user_data = {
                'first_name': user.first_name,
                'second_name': user.second_name,
                'department': user.department.name,
                'specialty': user.specialty.name,
                'group': user.group.name,
                'user_type': dict(CustomUser.type_choice).get(user.user_type),
                'image': user.image,
                "full_id": user.full_id

            }
            print(user_data)
            return JsonResponse({'success': True, 'user': user_data})
        except CustomUser.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User not found'}, status=404)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


def get_book_by_student_id(request):
    if request.method == 'GET':
        # `student_user_id` ni request parametrlaridan olish
        book_id = request.GET.get('book_id')
        if not book_id:
            return JsonResponse({'success': False, 'message': 'Student user ID not provided'}, status=400)

        try:
            # Foydalanuvchini qidirish
            book = Book.objects.get(book_id=book_id)
            print(book.added_by.full_name),

            # Foydalanuvchini JSON shaklida qaytarish
            book_data = {
                'title': book.title,
                'author': book.author,
                'publication_year': book.publication_year,
                'added_by': book.added_by.full_name,  # added_by field -> first_name
                'quantity': book.quantity,
                'available_quantity': book.available_quantity,
                'library': book.library.name,
                "book_id": book.book_id
            }
            print(book_data)
            return JsonResponse({'success': True, 'book': book_data})
        except CustomUser.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User not found'}, status=404)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


def add_book_loan(book, user, library, quantity):
    try:
        # Kitobni foydalanuvchiga biriktirish
        BookLoan.objects.create(
            book=book,
            user=user,
            library=library,
            status='pending',  # Kutilmoqda
            quantity= quantity
        )

        # Biriktirilgan kitobni `available_quantity` ni kamaytiramiz
        book.available_quantity = F('available_quantity') - 1
        book.save()

        return True, "Kitob muvaffaqiyatli biriktirildi."
    except Exception as e:
        return False, str(e)


@require_POST
def book_loan_library(request):
    if request.is_ajax():
        book_id = request.POST.get('book_id')
        full_id = request.POST.get('full_id')
        quantity = request.POST.get('quantity_book')

        try:
            book = Book.objects.get(pk=book_id)
            user = CustomUser.objects.get(pk=full_id)
            library = request.user.library

            success, message = add_book_loan(book, user, library, quantity)
            if success:
                return JsonResponse({'message': message}, status=200)
            else:
                return JsonResponse({'error': message}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Xatolik yuz berdi.'}, status=400)
