from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from account.models import CustomUser
from .forms import OnlineBookForm, BookLoanForm
from .models import Book, BookLoan, OnlineBook, BookOrder


# def check_user_role(user, allowed_roles):
#     return user.is_authenticated and user.user_role in allowed_roles

def library_dashboard(request):
    """Bosh sahifa ko'rsatkichi."""
    # Foydalanuvchi admin yoki librarian bo'lsa
    # if request.user.is_authenticated and (request.user.is_staff or request.user.groups.filter(name='Admin').exists()):
    # Foydalanuvchi bilan bog'liq kutubxona obyekti
    user_library = request.user.library.library

    # Kitoblar soni
    book_count = Book.objects.filter(library=user_library).count()

    # Obunachilar soni
    # subscribers_count = CustomUser.objects.filter(user_role='book_subscriber').count()

    # Onlayn kitoblar soni
    online_books_count = OnlineBook.objects.count()

    # Buyurtma qilingan kitoblar soni
    ordered_books_count = BookOrder.objects.filter(status='pending').count()

    context = {
        'book_count': book_count,
        # 'subscribers_count': subscribers_count,
        'online_books_count': online_books_count,
        'ordered_books_count': ordered_books_count,
    }

    return render(request, 'app/library/layout/index.html', context)
    # else:
    #     return HttpResponseForbidden("Sizga bu sahifaga kirish uchun ruxsat yo'q.")

def library_views(request):
    return render(request , 'app/library/pages/librarys.html')


@login_required
def book_list(request):
    """Kitoblar ro'yxati sahifasi."""

    return render(request, 'app/library/pages/book_list.html')


@login_required
def add_book_view(request):
    """Yangi kitob qo'shish sahifasi."""
    return render(request, 'app/library/pages/add_book.html')


@login_required
def busy_book(request):
    """Band kitoblar ro'yxati sahifasi."""

    busy_books = BookLoan.objects.filter(status='pending')
    return render(request, 'app/library/pages/busy_book.html', {'busy_books': busy_books})


@login_required
def online_book_list(request):
    """Online kitoblar ro'yhati."""
    online_books = OnlineBook.objects.all()
    return render(request, 'app/library/pages/online_book_list.html', {'online_books': online_books})


@login_required
def add_online_book(request):
    """Onlayn kitob qo'shish sahifasi."""
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
    # subscribers = CustomUser.objects.filter(user_role='book_subscriber')
    return render(request, 'app/library/pages/followers_book.html', )


@login_required
def add_followers_book(request):
    """Obunachiga kitob qo'shish sahifasi."""
    return render(request, 'app/library/pages/add_followers_book.html')


@login_required
def qarzdor_kitobhon(request):
    """Qarzdor kitoblar ro'yxati sahifasi."""
    no_return_users = BookLoan.objects.filter(status='not_returned').values_list('user__username', flat=True).distinct()
    return render(request, 'app/library/pages/qarzdor_kitobhon.html', {'no_return_users': no_return_users})


@login_required
def give_book(request):
    """Kitob olib borish qo'shish."""
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
