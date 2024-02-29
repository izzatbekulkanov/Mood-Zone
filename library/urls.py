from django.urls import path
from .views import (library_dashboard,
                    book_list,
                    add_book,
                    busy_book,
                    online_book_list,
                    order_book,
                    followers_book,
                    attach_book,
                    attachment_book)

urlpatterns = [
    path('', library_dashboard, name='library_dashboard'),
    path('book_list', book_list, name='book_list'),
    path('add_book', add_book, name='add_book'),
    path('busy_book', busy_book, name='busy_book'),
    path('online_book', online_book_list, name='online_book'),
    path('order_book', order_book, name='order_book'),
    path('followers_book', followers_book, name='followers_book'),
    path('attach_book', attach_book, name='attach_book'),
    path('attachment_book', attachment_book, name='attachment_book'),
]
