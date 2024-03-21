from django.urls import path

from .bookLeanViews import get_user_by_student_id, get_book_by_student_id, book_loan_library
from .bookViews import save_book, book_list_json, change_book_status, edit_book
from .libraryViews import create_library_json, libraries_list
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
                    give_book, library_views,
                    )

# URLs related to books
book_urls = [
    path('get_user_by_student_id', get_user_by_student_id, name='get_user_by_student_id'),
    path('get_book_by_student_id', get_book_by_student_id, name='get_book_by_student_id'),
    path('book_loan_library', book_loan_library, name='book_loan_library'),
    path('book_list', book_list, name='book_list'),
    path('add_book', add_book_view, name='add_book'),
    path('busy_book', busy_book, name='busy_book'),
    path('online_book_list', online_book_list, name='online_book'),
    path('add_online_book', add_online_book, name='add_online_book'),
    path('order_book', order_book, name='order_book'),
    path('followers_book', followers_book, name='followers_book'),
    path('add_followers_book', add_followers_book, name='add_followers_book'),
    path('debtors_book', qarzdor_kitobhon, name='qarzdor_kitobhon'),
    path('statistics_book', statistics_book, name='statistics_book'),
    path('give_book', give_book, name='give_book'),
    path('save_book', save_book, name='save_book'),
    path('book_list_json', book_list_json),
    path('change_book_status/<int:book_id>/', change_book_status, name='change_book_status'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book')
]

# URLs related to libraries
library_urls = [
    path('', library_dashboard, name='library_dashboard'),
    path('librarys', library_views, name='library_views'),
    path('create_library_json/', create_library_json, name='create_library_json'),
    path('libraries_list/', libraries_list, name='libraries_list')
]

# Combining both URL lists into urlpatterns
urlpatterns = book_urls + library_urls
