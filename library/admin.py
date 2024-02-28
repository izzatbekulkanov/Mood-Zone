from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'quantity', 'isbn', 'publication_year', 'created_at', 'updated_at']
    list_filter = ['author', 'publication_year', 'created_at', 'updated_at']
    search_fields = ['title', 'author', 'isbn']
    readonly_fields = ['created_at', 'updated_at']
    filter_horizontal = ['borrowed_by']
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'isbn', 'publication_year', 'image', 'quantity', 'borrowed_by')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
