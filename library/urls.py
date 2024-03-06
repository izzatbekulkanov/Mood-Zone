from django.urls import path
from .views import (library_dashboard,
                    book_list,
                    add_book_view,
                    busy_book,
                    online_book_list,
                    add_online_book,
                    order_book,
                    followers_book,
                    add_followers_book,
                    qarzdor_kitobhon,
                    statistics_book,
                    give_book,
                    save_book,
                    book_list_json,
                    change_book_status, edit_book,
                    )

urlpatterns = [
    # Kutubxona bosh sahifasi
    path('', library_dashboard, name='library_dashboard'),

    # Kitoblar ro'yxati
    path('book_list', book_list, name='book_list'),

    # Yangi kitob qo'shish
    path('add_book', add_book_view, name='add_book'),

    # Band kitoblar ro'yxati
    path('busy_book', busy_book, name='busy_book'),

    # Online kitoblar ro'yxati
    path('online_book_list', online_book_list, name='online_book'),

    # Onlayn kitob qo'shish
    path('add_online_book', add_online_book, name='add_online_book'),

    # Kitob buyurtma
    path('order_book', order_book, name='order_book'),

    # Obunachilar ro'yxati
    path('followers_book', followers_book, name='followers_book'),

    # Obunachiga kitob qo'shish
    path('add_followers_book', add_followers_book, name='add_followers_book'),

    # Qarzdor kitoblar ro'yxati
    path('debtors_book', qarzdor_kitobhon, name='qarzdor_kitobhon'),

    # Statistika
    path('statistics_book', statistics_book, name='statistics_book'),

    # Kitob olib bormoq
    path('give_book', give_book, name='give_book'),

    # Kitobni saqlash
    path('save_book', save_book, name='save_book'),

    # JSON formatidagi kitoblar ro'yxati
    path('book_list_json', book_list_json),

    # Kitob holatini o'zgartirish
    path('change_book_status/<int:book_id>/', change_book_status, name='change_book_status'),

    # Kitob holatini o'zgartirish
    path('edit_book/<int:book_id>/', edit_book, name='edit_book')
]
