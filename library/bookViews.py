import json
from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models.functions import Lower
from django.http import JsonResponse
from django.utils import formats, timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from core import settings
from library.models import Book, Author, BookType, AdminLibrary


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
            'authors': [author.name for author in book.authors.all()],  # Mualliflarni ro'yxat sifatida qo'shing
            'quantity': book.quantity,
            'book_id': book.book_id,
            'isbn': book.isbn,
            'publication_year': book.publication_year,
            'created_at': formats.date_format(book.created_at, "Y-m-d | H:i"),
            'status': book.status,
            'added_by': book.added_by.full_name,
            'library_name': book.library.name if book.library else None,  # Kitobning kutubhona nomi (agar mavjud bo'lsa)
            'book_type': book.book_type.name if book.book_type else None  # Kitob turi nomi
        }
        latest_books_data.append(latest_book_info)
    for book in approved_books:
        book_info = {
            'title': book.title,
            'authors': [author.name for author in book.authors.all()],  # Mualliflarni ro'yxat sifatida qo'shing
            'quantity': book.quantity,
            'book_id': book.book_id,
            'isbn': book.isbn,
            'publication_year': book.publication_year,
            'status': book.status,
            'added_by': book.added_by.full_name,
            'library_name': book.library.name if book.library else None, # Kitobning kutubhona nomi (agar mavjud bo'lsa)
            'book_type': book.book_type.name if book.book_type else None  # Kitob turi nomi
        }
        approved_book_data.append(book_info)
    for book in rejected_books:
        rejected_book_info = {
            'title': book.title,
            'authors': [author.name for author in book.authors.all()],  # Mualliflarni ro'yxat sifatida qo'shing
            'quantity': book.quantity,
            'book_id': book.book_id,
            'isbn': book.isbn,
            'publication_year': book.publication_year,
            'status': book.status,
            'added_by': book.added_by.full_name,
            'library_name': book.library.name if book.library else None,  # Kitobning kutubhona nomi (agar mavjud bo'lsa)
            'book_type': book.book_type.name if book.book_type else None  # Kitob turi nomi
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

def get_book_types(request):
    book_types = BookType.objects.annotate(book_count=Count('books')).order_by(Lower('name'))
    data = list(book_types.values('id', 'name', 'book_count', 'image', 'id'))  # Ma'lumotlarni to'plash
    for item in data:
        if item['image']:
            item['image_url'] = settings.MEDIA_URL + item['image']  # Rasm URL sini qo'shish
    return JsonResponse(data, safe=False)

@require_POST
def create_book_type(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Name of the book type
        image = request.FILES.get('image')  # Image file for the book type

        # Check if the name is provided
        if not name:
            return JsonResponse({'error': 'Name is required.'}, status=400)

        try:
            existing_book_type = BookType.objects.get(name=name)
            return JsonResponse({'error': f'Book type "{name}" already exists.', 'id': existing_book_type.id}, status=400)
        except ObjectDoesNotExist:
            # Create the new book type
            book_type = BookType.objects.create(name=name, image=image)

            # Return success response
            return JsonResponse({'message': 'Book type created successfully.', 'id': book_type.id}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

@require_POST
def save_book_type_image(request):
    book_type_id = request.POST.get('book_type_id')
    image = request.FILES.get('image')

    try:
        # Sizning saqlash logikangiz
        # Masalan:
        book_type = BookType.objects.get(pk=book_type_id)
        name = book_type.name
        book_type.image = image
        book_type.save()

        # Tasvir URL manzilini qaytarish
        image_url = book_type.image.url if book_type.image else None

        return JsonResponse({'message': 'Rasm muvaffaqiyatli biriktirildi.', 'image_url': image_url, 'name': name})
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Book type not found.'}, status=404)

def save_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        authors_input = request.POST.get('author')  # Mualliflarni ajratilgan matn sifatida qabul qilamiz

        # Mualliflarni ajratib olish
        author_names = [name.strip() for name in authors_input.split(',') if name.strip()]
        authors = []
        for author_name in author_names:
            author, created = Author.objects.get_or_create(name=author_name)
            authors.append(author)

        isbn = request.POST.get('isbn')
        image = request.FILES.get('image')
        book_file = request.FILES.get('bookFile')
        publication_year = request.POST.get('publication_year')
        quantity = request.POST.get('quantity')
        language = request.POST.get('language')
        pages = request.POST.get('pages')
        publisher = request.POST.get('publisher')
        published_city = request.POST.get('published_city')
        annotation = request.POST.get('annotation')
        status = request.POST.get('status')

        try:
            user_admin_library = AdminLibrary.objects.get(user=request.user)
            user_library = user_admin_library.library
        except ObjectDoesNotExist:
            user_library = None

        book_type_id = request.POST.get('bookType')
        book_type = BookType.objects.get(id=book_type_id)

        # Yangi kitob obyektini yaratish
        book = Book(
            title=title,
            isbn=isbn,
            image=image,
            file=book_file,
            publication_year=publication_year,
            quantity=quantity,
            available_quantity=quantity,
            language=language,
            publisher=publisher,
            published_city=published_city,
            pages=pages,
            annotation=annotation,
            status=status,
            library=user_library,
            added_by=request.user,
            book_type=book_type,
        )
        book.save()  # Kitob obyektini saqlash

        # Kitobga mualliflarni qo'shish
        book.authors.add(*authors)

        return JsonResponse({'message': 'Ma\'lumotlar muvaffaqiyatli saqlandi.'}, status=200)
    else:
        return JsonResponse({'error': 'Faqat POST so\'rov qabul qilinadi.'}, status=405)
