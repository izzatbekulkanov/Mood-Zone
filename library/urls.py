from django.urls import path

from .authorsViews import get_authors
from .bookLeanViews import get_user_by_student_id, get_book_by_student_id, book_loan_library
from .bookViews import save_book, book_list_json, change_book_status, edit_book, get_book_types, create_book_type, \
    save_book_type_image
from .followersViews import create_follower_from_api
from .libraryViews import create_library_json, libraries_list, get_library_users, add_librarian, \
    soft_delete_admin_library, send_library_group_users
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
                    give_book, library_views, book_type_list, book_author_view,
                    )

# URLs related to books
book_urls = [
    path('get_user_by_student_id', get_user_by_student_id, name='get_user_by_student_id'),
    path('get_book_by_student_id', get_book_by_student_id, name='get_book_by_student_id'),
    path('book_loan_library', book_loan_library, name='book_loan_library'),
    path('book_list', book_list, name='book_list'),
    path('book_type_list', book_type_list, name='book_type_list'),
    path('create_book_type', create_book_type, name='create_book_type'),
    path('save_book_type_image', save_book_type_image, name='save_book_type_image'),
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
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('get_book_types/', get_book_types, name='get_book_types'),

]

author_urls = [
    path('authors', book_author_view, name='book_author_list'),
    path('get_authors', get_authors, name='get_authors'),
]

# URLs related to libraries
library_urls = [
    path('', library_dashboard, name='library_dashboard'),
    path('librarys', library_views, name='library_views'),
    path('add_librarian', add_librarian, name='add_librarian'),
    path('soft_delete_admin_library/<int:admin_library_id>/', soft_delete_admin_library, name='soft_delete_admin_library'),
    path('get_library_users', get_library_users, name='get_library_users'),
    path('create_library_json/', create_library_json, name='create_library_json'),
    path('libraries_list/', libraries_list, name='libraries_list'),
    path('send_library_group_users', send_library_group_users, name='send_library_group_users')
]

follower_urls = [
    path('create_follower_from_api', create_follower_from_api, name='create_follower_from_api'),
]

# Combining both URL lists into urlpatterns
urlpatterns = book_urls + author_urls +library_urls + follower_urls
