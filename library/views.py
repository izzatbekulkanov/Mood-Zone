from django.shortcuts import render


# Create your views here.


def library_dashboard(request):
    return render(request, 'app/library/layout/index.html')
def book_list(request):
    return render(request, 'app/library/book_list.html')


def add_book(request):
    return render(request, 'app/library/add_book.html')


def online_book_list(request):
    return render(request, 'app/library/online_book_list.html')


def order_book(request):
    return render(request, 'app/library/order_book.html')


def attach_book(request):

    return render(request, 'app/library/attach_book.html')

def attachment_book(request):

    return render(request, 'app/library/attachment_book.html')
