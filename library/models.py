from django.db import models
from account.models import CustomUser


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    isbn = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    publication_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    borrowed_by = models.ManyToManyField(CustomUser, related_name='borrowed_books', blank=True)

    def __str__(self):
        return self.title