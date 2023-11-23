from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ["username", "first_name", "last_name", "verified", "email"]
    search_fields = ["username", "first_name", "last_name"]

