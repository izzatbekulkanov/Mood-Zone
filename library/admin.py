from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Library, Book, BookLoan, AdminLibrary, OnlineBook, BookOrder


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created_date', 'updated_date']
    search_fields = ['name', 'address']
    readonly_fields = ['created_date', 'updated_date']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'quantity', 'available_quantity' , 'book_id', 'publication_year', 'status', 'added_by_full_name',
                    'library', 'barcode_display']
    list_editable = ['status', 'library']
    list_filter = ['author', 'publication_year', 'created_at', 'updated_at', 'library']
    search_fields = ['title', 'author', 'book_id']
    readonly_fields = ['created_at', 'updated_at', 'added_by']
    fieldsets = (
        (None, {
            'fields': (
                'title', 'author', 'quantity', 'available_quantity', 'book_id', 'image', 'publication_year', 'library', 'status', 'added_by',
                'isbn')
        }),
        ("Vaqt ma'lumotlari", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def barcode_display(self, obj):
        """Bar code qismi uchun rasmini ko'rsatish."""
        if obj.barcode_book:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.barcode_book.url,
                width=100,
                height=50,
            ))
        return "No barcode"

    barcode_display.short_description = 'Barcode Image'

    def added_by_full_name(self, obj):
        """Foydalanuvchi to'liq ismini qaytarish."""
        if obj.added_by:
            return obj.added_by.full_name
        return "Unknown"

    added_by_full_name.short_description = 'Added By'

    def custom_status(self, obj):
        """Statusni tahrirlash."""
        return obj.status.capitalize() if obj.status else ""

    custom_status.short_description = 'Status'



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


@admin.register(BookOrder)
class BookOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'book_title', 'author', 'order_date', 'status']
    list_filter = ['status', 'order_date']
    search_fields = ['user__email', 'book_title', 'author']
    readonly_fields = ['order_date']
