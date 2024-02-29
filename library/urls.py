from django.urls import path
from .views import (library_dashboard,
                    book_list,
                    add_book,
                    busy_book,
                    online_book_list,
                    add_online_book,
                    order_book,
                    followers_book,
                    add_followers_book,
                    qarzdor_kitobhon,
                    statistics_book,
                    give_book)

urlpatterns = [
    path('', library_dashboard, name='library_dashboard'),
    path('book_list', book_list, name='book_list'),
    path('add_book', add_book, name='add_book'),
    path('busy_book', busy_book, name='busy_book'),
    path('online_book_list', online_book_list, name='online_book'),
    path('add_online_book', add_online_book, name='add_online_book'),
    path('order_book', order_book, name='order_book'),
    path('followers_book', followers_book, name='followers_book'),
    path('add_followers_book', add_followers_book, name='add_followers_book'),
    path('debtors_book', qarzdor_kitobhon, name='qarzdor_kitobhon'),
    path('statistics_book', statistics_book, name='statistics_book'),
    path('give_book', give_book, name='give_book')
]
