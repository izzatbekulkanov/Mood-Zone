import json
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import formats, timezone
from django.views.decorators.csrf import csrf_exempt

from library.models import Book


def book_list_json(request):
    # Oxirgi 1 soat ichida kiritilgan kitoblarni olish
    last_hour = timezone.now() - timedelta(hours=1)
    """Kitoblar va ularning kutubhonalari ro'yxati."""
    # Oxirgi 1 soat ichida kiritilgan barcha kitoblarni olish
    latest_books = Book.objects.filter(created_at__gte=last_hour)
    approved_books = Book.objects.filter(status='accepted')  # Tasdiqlangan kitoblarni olish
    rejected_books = Book.objects.filter(status='rejected')  # Rad etilgan kitoblarni olish

    # Kitoblar va ularning kutubhonalari haqida ma'lumotlar
    approved_book_data = []
    rejected_book_data = []
    latest_books_data = []
    for book in latest_books:
        latest_book_info = {
            'title': book.title,
            'author': book.author,
            'quantity': book.quantity,
            'book_id': book.book_id,
            'isbn': book.isbn,
            'publication_year': book.publication_year,
            'created_at': formats.date_format(book.created_at, "Y-m-d | H:i"),
            'status': book.status,
            'added_by': book.added_by.full_name,
            'library_name': book.library.name if book.library else None  # Kitobning kutubhona nomi (agar mavjud bo'lsa)
        }
        latest_books_data.append(latest_book_info)
    for book in approved_books:
        book_info = {
            'title': book.title,
            'author': book.author,
            'quantity': book.quantity,
            'book_id': book.book_id,
            'isbn': book.isbn,
            'publication_year': book.publication_year,
            'status': book.status,
            'added_by': book.added_by.full_name,
            'library_name': book.library.name if book.library else None  # Kitobning kutubhona nomi (agar mavjud bo'lsa)
        }
        approved_book_data.append(book_info)
    for book in rejected_books:
        rejected_book_info = {
            'title': book.title,
            'author': book.author,
            'quantity': book.quantity,
            'book_id': book.book_id,
            'isbn': book.isbn,
            'publication_year': book.publication_year,
            'status': book.status,
            'added_by': book.added_by.full_name,
            'library_name': book.library.name if book.library else None  # Kitobning kutubhona nomi (agar mavjud bo'lsa)
        }
        rejected_book_data.append(rejected_book_info)
    # JSON ma'lumotlarni tayyorlash
    data = {
        'approved_books': approved_book_data,  # Tasdiqlangan kitoblarni JSON formatida
        'rejected_books': rejected_book_data,  # Rad etilgan kitoblarni JSON formatida
        'latest_books': latest_books_data,  # Ohirgi kiritilgan kitoblar royhati kitoblarni JSON formatida
    }
    # JSON javobini qaytarish
    return JsonResponse(data)


@csrf_exempt
def edit_book(request, book_id):
    if request.method == 'POST':
        try:
            # Kitob obyektini topish
            book = Book.objects.get(book_id=book_id)

            # JSON ma'lumotlarni olish
            data = json.loads(request.body)

            # Kitob ma'lumotlarini o'zgartirish
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            book.isbn = data.get('isbn', book.isbn)
            book.image = data.get('image', book.image)
            book.publication_year = data.get('publication_year', book.publication_year)
            book.quantity = data.get('quantity', book.quantity)
            book.status = data.get('status', book.status)

            # Kitobni saqlash
            book.save()

            # Yangilangan ma'lumotlarni JSON formatida qaytarish
            return JsonResponse({'message': 'Book updated successfully', 'data': {
                'title': book.title,
                'author': book.author,
                'isbn': book.isbn,
                'image': book.image,
                'publication_year': book.publication_year,
                'quantity': book.quantity,
                'status': book.status,
            }})
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
def change_book_status(request, book_id):
    if request.method == 'POST':
        try:
            book = Book.objects.get(book_id=book_id)
            book.status = 'accepted'  # Yangi status
            book.save()
            return JsonResponse({'success': True})  # JSON javobni qaytarish muvaffaqiyatli o'zgartirishni bildiradi
        except Book.DoesNotExist:
            return JsonResponse(
                {'success': False, 'error': 'Kitob topilmadi'})  # Agar kitob topilmagan bo'lsa xatolik bildiriladi

    # Agar POST so'rovi emas bo'lsa yoki kitob topilmagan bo'lsa
    return JsonResponse({'success': False, 'error': 'Noto\'g\'ri so\'rov tashlanadi'})

@login_required
def save_book(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        image = request.FILES.get('image')
        publication_year = request.POST.get('publication_year')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        user_library = request.user.library.library

        book = Book(
            title=title,
            author=author,
            isbn=isbn,
            image=image,
            publication_year=publication_year,
            quantity=quantity,
            status=status,
            library=user_library,
            added_by=request.user
        )
        book.save()

        return JsonResponse({'message': 'Ma\'lumotlar muvaffaqiyatli saqlandi.'}, status=200)
    else:
        return JsonResponse({'error': 'Faqat POST so\'rov qabul qilinadi.'}, status=405)