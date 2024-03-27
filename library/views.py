from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from account.models import CustomUser
from .forms import OnlineBookForm, BookLoanForm
from .models import Book, BookLoan, OnlineBook, BookOrder, BookType, AdminLibrary


def library_dashboard(request):
    if request.user.is_authenticated:
        if request.user.now_role in ['Library', 'Administrator']:
            try:
                admin_library = AdminLibrary.objects.get(user=request.user, is_deleted=False)
                library_book_count = admin_library.library.books.count()  # Kutubhonadagi kitoblar soni
                library_address = admin_library.library.address  # Kutubxona manzili
                library_name = admin_library.library.name  # Kutubxona nomi

                # is_followers_book alanı True olan kullanıcıların sayısı
                followers_book_count = CustomUser.objects.filter(is_followers_book=True).count()

                context = {
                    'library_address': library_address,
                    'library_name': library_name,
                    'library_book_count': library_book_count,
                    'followers_book_count': followers_book_count,
                }
                return render(request, 'app/library/dashboard.html', context)
            except AdminLibrary.DoesNotExist:
                pass  # Hata durumunda aşağıdaki kısımda kullanıcıyı yönlendireceğiz

        # "Library" veya "Administrator" grubuna üye olmayan kullanıcılar için
        return redirect('error')  # Hata URL'sine yönlendirme
    else:
        # Oturum açmamış kullanıcılar için
        return redirect('login')  # Giriş URL'sine yönlendirme

@login_required
def library_views(request):
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                return render(request, 'app/library/pages/librarys.html')
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')


def book_list(request):
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library']:
                if request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                    return render(request, 'app/library/pages/book_list.html')
                else:
                    return redirect(f'{user_url}_dashboard')
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')

@login_required
def book_type_list(request):
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                return render(request, 'app/library/pages/book_type.html')
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')

@login_required
def book_author_view(request):
    """Kitob mualliflari sahifasi."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                return render(request, 'app/library/pages/authors.html')
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')


@login_required
def add_book_view(request):
    """Yangi kitob qoshish."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                book_types = BookType.objects.all()
                return render(request, 'app/library/pages/add_book.html', {'book_types': book_types})
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')


@login_required
def busy_book(request):
    """Band Kitoblar."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                busy_books = BookLoan.objects.filter(status='pending')
                return render(request, 'app/library/pages/busy_book.html', {'busy_books': busy_books})
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')


@login_required
def online_book_list(request):
    """Online kitoblar."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                online_books = OnlineBook.objects.all()
                return render(request, 'app/library/pages/online_book_list.html', {'online_books': online_books})
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')


@login_required
def add_online_book(request):
    """Onlayn kitob qo'shish sahifasi."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                return render(request, 'app/library/pages/add_online_book.html')
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')


@login_required
def order_book(request):
    """Kitob buyurtma sahifasi."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                pending_orders = BookOrder.objects.filter(status='pending')
                approved_orders = BookOrder.objects.filter(status='approved')
                canceled_orders = BookOrder.objects.filter(status='canceled')

                context = {
                    'pending_orders': pending_orders,
                    'approved_orders': approved_orders,
                    'canceled_orders': canceled_orders,
                }
                return render(request, 'app/library/pages/order_book.html', context)
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')


@login_required
def followers_book(request):
    """Obunachilar ro'yxati sahifasi."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                return render(request, 'app/library/pages/followers_book.html')
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')

@login_required
def add_followers_book(request):
    """Obunachiga kitob qo'shish sahifasi."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                return render(request, 'app/library/pages/add_followers_book.html')
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')

@login_required
def qarzdor_kitobhon(request):
    """Qarzdor kitoblar ro'yxati sahifasi."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                no_return_users = BookLoan.objects.filter(status='not_returned').values_list('user__username', flat=True).distinct()
                return render(request, 'app/library/pages/qarzdor_kitobhon.html', {'no_return_users': no_return_users})
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')

@login_required
def give_book(request):
    """Kitob berish qo'shish."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
                no_return_users = BookLoan.objects.filter(status='not_returned').values_list('user__username', flat=True).distinct()
                return render(request, 'app/library/pages/give_book.html', {'no_return_users': no_return_users})
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')


@login_required
def statistics_book(request):
    """Statistika sahifasi."""
    if request.user.is_authenticated:
        user_url = request.user.now_role.lower()
        if request.user.groups.exists():
            if request.user.now_role in ['Administrator', 'Library'] and request.user.groups.filter(name__in=['Administrator', 'Library']).exists():
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
            else:
                return redirect(f'{user_url}_dashboard')
        else:
            return redirect('error')
    else:
        return redirect('login')

