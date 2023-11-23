from django.contrib import admin
from .models import Post, Action, Notification

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'body', 'likes', 'saveds', 'reposts', 'views', 'created', 'updated')
    list_filter = ('user', 'created', 'updated')
    search_fields = ('body', 'user__username')


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'action_type', 'users', 'posts', 'datetime')
    list_filter = ('action_type', 'users', 'posts', 'datetime')
    search_fields = ('action_type', 'users__username', 'posts__body')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'datetime', 'is_seen', 'to')
    list_filter = ('is_seen', 'to', 'datetime')
    search_fields = ('body', 'to__username')
