import json
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, JsonResponse
from django.utils import timezone, formats
from django.views.decorators.csrf import csrf_exempt

from account.models import CustomUser
from .forms import OnlineBookForm, BookLoanForm
from .models import Book, BookLoan, OnlineBook, BookOrder


def check_user_role(user, allowed_roles):
    return user.is_authenticated and user.user_role in allowed_roles


def library_dashboard(request):
    """Bosh sahifa ko'rsatkichi."""
    # Foydalanuvchi admin yoki librarian bo'lsa
    if check_user_role(request.user, ['admin', 'librarian']):
        # Foydalanuvchi bilan bog'liq kutubxona obyekti
        user_library = request.user.library.library

        # Kitoblar soni
        book_count = Book.objects.filter(library=user_library).count()

        # Obunachilar soni
        subscribers_count = CustomUser.objects.filter(user_role='book_subscriber').count()

        # Onlayn kitoblar soni
        online_books_count = OnlineBook.objects.count()

        # Buyurtma qilingan kitoblar soni
        ordered_books_count = BookOrder.objects.filter(status='pending').count()

        context = {
            'book_count': book_count,
            'subscribers_count': subscribers_count,
            'online_books_count': online_books_count,
            'ordered_books_count': ordered_books_count,
        }

        return render(request, 'app/library/layout/index.html', context)
    else:
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")


@login_required
def book_list(request):
    """Kitoblar ro'yxati sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")

    return render(request, 'app/library/pages/book_list.html')


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
    if request.method == 'PUT':
        try:
            # Kitobni bazadan izlash
            book = Book.objects.get(id=book_id)

            # JSON ma'lumotlarni qabul qilish
            data = json.loads(request.body)

            # Ma'lumotlarni yangilash
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            book.quantity = data.get('quantity', book.quantity)
            book.publication_year = data.get('publication_year', book.publication_year)
            book.status = data.get('status', book.status)
            book.library = data.get('library', book.library)

            # Ma'lumotlarni saqlash
            book.save()

            # Yangilangan ma'lumotlarni JSON formatida qaytarish
            return JsonResponse({'message': 'Book updated successfully', 'data': {
                'title': book.title,
                'author': book.author,
                'quantity': book.quantity,
                'publication_year': book.publication_year,
                'status': book.status,
                'library': book.library
            }})
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)
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
def add_book_view(request):
    """Yangi kitob qo'shish sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    return render(request, 'app/library/pages/add_book.html')


@login_required
def save_book(request):
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga kitob kiritishga ruhsat yo'q.")
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


@login_required
def busy_book(request):
    """Band kitoblar ro'yxati sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    busy_books = BookLoan.objects.filter(status='pending')
    return render(request, 'app/library/pages/busy_book.html', {'busy_books': busy_books})


@login_required
def online_book_list(request):
    """Online kitoblar ro'yhati."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    online_books = OnlineBook.objects.all()
    return render(request, 'app/library/pages/online_book_list.html', {'online_books': online_books})


@login_required
def add_online_book(request):
    """Onlayn kitob qo'shish sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    if request.method == 'POST':
        form = OnlineBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('online_book_list')  # Online kitoblar ro'yxatiga o'tish
    else:
        form = OnlineBookForm()
    return render(request, 'app/library/pages/add_online_book.html', {'form': form})


@login_required
def order_book(request):
    """Kitob buyurtma sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    pending_orders = BookOrder.objects.filter(status='pending')
    approved_orders = BookOrder.objects.filter(status='approved')
    canceled_orders = BookOrder.objects.filter(status='canceled')

    context = {
        'pending_orders': pending_orders,
        'approved_orders': approved_orders,
        'canceled_orders': canceled_orders,
    }

    return render(request, 'app/library/pages/order_book.html', context)


@login_required
def followers_book(request):
    """Obunachilar ro'yxati sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    subscribers = CustomUser.objects.filter(user_role='book_subscriber')
    return render(request, 'app/library/pages/followers_book.html', {'subscribers': subscribers})


@login_required
def add_followers_book(request):
    """Obunachiga kitob qo'shish sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    return render(request, 'app/library/pages/add_followers_book.html')


@login_required
def qarzdor_kitobhon(request):
    """Qarzdor kitoblar ro'yxati sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    no_return_users = BookLoan.objects.filter(status='not_returned').values_list('user__username', flat=True).distinct()
    return render(request, 'app/library/pages/qarzdor_kitobhon.html', {'no_return_users': no_return_users})


@login_required
def give_book(request):
    """Kitob olib borish qo'shish."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    if request.method == 'POST':
        form = BookLoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book_loan')  # Yoki kerakli boshqa yo'lda o'tishni ko'rsating
    else:
        form = BookLoanForm()
    return render(request, 'app/library/pages/give_book.html', {'form': form})


@login_required
def statistics_book(request):
    """Statistika sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    # Obunachilari soni
    subscribers_count = CustomUser.objects.filter(user_role='book_subscriber').count()

    # Kitoblar soni
    books_count = Book.objects.all().count()

    # Online kitoblar soni
    online_books_count = OnlineBook.objects.all().count()

    # Biriktirilgan kitoblar soni
    loaned_books_count = BookLoan.objects.filter(status='pending').count()

    # Kutilmoqda tasdiqlangan va to'xtatilgan buyurtma kitoblarning soni
    pending_orders_count = BookLoan.objects.filter(status='pending').count()
    returned_orders_count = BookLoan.objects.filter(status='returned').count()

    # Shu oy davomida nechta obunachiga kitob berilgani soni
    current_month = timezone.now().month
    current_month_loans_count = BookLoan.objects.filter(loan_date__month=current_month).count()

    # Nechta obunachidan kitob qaytarib olingani soni
    returned_books_count = BookLoan.objects.filter(status='returned').count()

    # Chiqarib berilgan kitoblar soni
    issued_books_count = BookLoan.objects.exclude(status='returned').count()

    context = {
        'subscribers_count': subscribers_count,
        'books_count': books_count,
        'online_books_count': online_books_count,
        'loaned_books_count': loaned_books_count,
        'pending_orders_count': pending_orders_count,
        'returned_orders_count': returned_orders_count,
        'current_month_loans_count': current_month_loans_count,
        'returned_books_count': returned_books_count,
        'issued_books_count': issued_books_count,
    }
    return render(request, 'app/library/pages/statistics.html', context)
