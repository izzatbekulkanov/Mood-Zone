from account.models import CustomUser
import random
import string
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def validate_file_extension(value):
    """Faylning formatini tekshirish uchun validator."""
    if value.content_type not in ['application/pdf', 'application/msword',
                                  'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        raise ValidationError("Faqat PDF va Word formatidagi fayllarni yuklash mumkin.")


def generate_book_id():
    """Kitob identifikatorini avtomatik tarzda yaratish."""
    return '309' + ''.join(random.choices(string.digits, k=6))


class Library(models.Model):
    name = models.CharField(max_length=255, help_text="Kutubhona nomi")
    address = models.CharField(max_length=255, help_text="Manzili")
    created_date = models.DateField(auto_now_add=True, help_text="Model yaratilgan sana")
    updated_date = models.DateField(auto_now=True, help_text="Model yangilangan sana")

    def __str__(self):
        return self.name


class Book(models.Model):
    """Kitob modeli."""
    title = models.CharField(max_length=255, help_text="Kitobning sarlavhasi")
    author = models.CharField(max_length=255, help_text="Kitobning muallifi")
    quantity = models.IntegerField(default=0, help_text="Kitoblar soni")
    book_id = models.CharField(max_length=9, default=generate_book_id, unique=True, help_text="Kitob identifikatori")
    image = models.ImageField(upload_to='book_covers/', blank=True, null=True, help_text="Kitob rasmi (mavjud bo'lsa)")
    publication_year = models.IntegerField(help_text="Kitobning nashr yili")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Kitob yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, help_text="Kitob oxirgi yangilanish vaqti")
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='books', null=True, blank=True,
                                help_text="Kitob kutubxonasi")

    def __str__(self):
        return self.title


class BookLoan(models.Model):
    """Kitob berish modeli."""
    book = models.ForeignKey('Book', on_delete=models.CASCADE, help_text="Kitob")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, help_text="Foydalanuvchi")
    loan_date = models.DateTimeField(default=timezone.now, help_text="Kitob olingan vaqti")
    STATUS_CHOICES = [
        ('pending', 'kutilmoqda'),
        ('returned', 'qaytarilgan'),
        ('not_returned', 'qaytarilmadi'),  # Qo'shimcha holat
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', help_text="Kitob holati")
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='book_loans', null=True, blank=True,
                                help_text="Kitob beriladigan kutubxona")

    def __str__(self):
        return f"{self.book} - {self.user}"

    def check_return_status(self):
        """Kitobni qaytarilganligini tekshirish."""
        if self.status != 'returned':
            loan_duration = timezone.now() - self.loan_date
            if loan_duration.days > 7:
                self.status = 'not_returned'
                self.save()
                return True
        return False


class AdminLibrary(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='library')
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return f"{self.user.username}'s Library"


def assign_library_to_librarians():
    librarians = CustomUser.objects.filter(user_role='librarian')
    for librarian in librarians:
        if not AdminLibrary.objects.filter(user=librarian).exists():
            # Agar bu foydalanuvchiga hali kutubxona biriktirilmagan bo'lsa, uni kutubxonaga biriktiramiz
            library = Library.objects.create(name=f"{librarian.username}'s Library")
            AdminLibrary.objects.create(user=librarian, library=library)


class OnlineBook(models.Model):
    """Onlayn kitob modeli."""
    online_book_id = models.CharField(max_length=9, default=generate_book_id, unique=True,
                                      help_text="Onlayn kitob identifikatori")
    name = models.CharField(max_length=255, help_text="Onlayn kitob nomi")
    content = models.TextField(help_text="Onlayn kitob mazmuni")
    created_date = models.DateTimeField(auto_now_add=True, help_text="Onlayn kitob yaratilgan vaqti")
    file = models.FileField(upload_to='online_books/', validators=[validate_file_extension],
                            help_text="Onlayn kitob fayli")

    def __str__(self):
        return self.name


class BookOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Kutilmoqda'),
        ('approved', 'Tasdiqlangan'),
        ('canceled', 'To\'xtatilgan'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.book_title} - {self.user}"
