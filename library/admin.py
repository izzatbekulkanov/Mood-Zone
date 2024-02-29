from django.contrib import admin
from .models import Library, Book, BookLoan, AdminLibrary, OnlineBook

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created_date', 'updated_date']
    search_fields = ['name', 'address']
    readonly_fields = ['created_date', 'updated_date']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'quantity', 'book_id', 'publication_year', 'created_at', 'updated_at', 'library']
    list_filter = ['author', 'publication_year', 'created_at', 'updated_at', 'library']
    search_fields = ['title', 'author', 'book_id']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'quantity', 'book_id', 'image', 'publication_year', 'library')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'loan_date', 'status', 'library']
    list_filter = ['status', 'loan_date', 'library']
    search_fields = ['book__title', 'user__username']
    readonly_fields = ['loan_date']
    fieldsets = (
        (None, {
            'fields': ('book', 'user', 'loan_date', 'status', 'library')
        }),
    )

@admin.register(AdminLibrary)
class AdminLibraryAdmin(admin.ModelAdmin):
    list_display = ['user', 'library']

@admin.register(OnlineBook)
class OnlineBookAdmin(admin.ModelAdmin):
    list_display = ['name', 'online_book_id', 'created_date']
    search_fields = ['name', 'online_book_id']
    readonly_fields = ['created_date']
