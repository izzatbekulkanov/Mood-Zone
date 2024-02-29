from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.utils import timezone

from account.models import CustomUser, BookOrder
from .forms import BookForm, OnlineBookForm, BookLoanForm
from .models import Book, BookLoan, OnlineBook


def check_user_role(user, allowed_roles):
    return user.is_authenticated and user.user_role in allowed_roles


def library_dashboard(request):
    """Bosh sahifa ko'rsatkichi."""
    # Foydalanuvchi admin yoki librarian bo'lsa
    if check_user_role(request.user, ['admin', 'librarian']):
        # Foydalanuvchiga tegishli kutubxona obunachilari soni
        library_subscribers = request.user.library.librarians.all()

        # Foydalanuvchiga tegishli kutubxona kitoblari
        library_books = request.user.library.books.all()

        # Foydalanuvchiga tegishli kutubxona online kitoblar
        library_online_books = request.user.library.onlinebook_set.all()

        # Foydalanuvchiga tegishli kutubxona buyurtma kitoblar
        library_pending_orders = request.user.library.bookorder_set.filter(status='pending')

        context = {
            'library_subscribers': library_subscribers,
            'library_books': library_books,
            'library_online_books': library_online_books,
            'library_pending_orders': library_pending_orders,
        }
        return render(request, 'app/library/layout/index.html', context)
    else:
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")

@login_required
def book_list(request):
    """Kitoblar ro'yxati sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    books = Book.objects.all()  # Barcha kitoblarni olish
    return render(request, 'app/library/pages/book_list.html', {'books': books})


@login_required
def add_book(request):
    """Yangi kitob qo'shish sahifasi."""
    if not check_user_role(request.user, ['admin', 'librarian']):
        return HttpResponseForbidden("Sizga bu sahifaga kirish huquqi yo'q.")
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_book')  # Yangi kitob saqlanganidan so'ng o'ziga qaytaradi
    else:
        form = BookForm()
    return render(request, 'app/library/pages/add_book.html', {'form': form})


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

