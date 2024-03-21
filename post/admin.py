from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at', 'updated_at', 'news_type', 'is_published']
    list_filter = ['created_by', 'created_at', 'updated_at', 'news_type', 'is_published']
    search_fields = ['title', 'description', 'main_info']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'main_info', 'image', 'created_by', 'news_type', 'is_published')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
