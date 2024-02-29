from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import BookForm
from .models import Book
from account.models import CustomUser


# Create your views here.


def library_dashboard(request):
    return render(request, 'app/library/layout/index.html')
def book_list(request):
    return render(request, 'app/library/pages/book_list.html')


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_book')  # Ushbu yo'lga o'ting, qaysi sahifaga o'tish kerakligini o'rnating
    else:
        form = BookForm()
    return render(request, 'app/library/pages/add_book.html', {'form': form})

def busy_book(request):
    return render(request, 'app/library/pages/busy_book.html')


def online_book_list(request):
    return render(request, 'app/library/online_book_list.html')


def order_book(request):
    return render(request, 'app/library/pages/order_book.html')
def borrow_book(request, user_id):
    if request.method == 'POST':
        # Kitob obyekti yaratish
        book = Book.objects.create(
            title="Kitob nomi",
            author="Muallif nomi",
            quantity=10,
            isbn="1234567890",
            image=None,  # Rasmdagi qiymatni qo'shing
            publication_year=2023
        )

        # Foydalanuvchini olish
        user = CustomUser.objects.get(pk=user_id)  # foydalanuvchi ID raqami

        # Kitobni iqtibos qilish
        book.borrowed_by = user
        book.borrowed_at = timezone.now()
        book.save()

        return HttpResponse('Kitob muvaffaqiyatli iqtibos qilindi!')
    else:
        return HttpResponse("Faqat POST so'rovlarni qabul qilamiz!")
def followers_book(request):
    return render(request, 'app/library/pages/followers_book.html')
def add_followers_book(request):
    return render(request, 'app/library/pages/add_followers_book.html')


def attach_book(request):

    return render(request, 'app/library/attach_book.html')

def attachment_book(request):

    return render(request, 'app/library/attachment_book.html')
