from datetime import timedelta
from io import BytesIO
import random
import string
from django.core.exceptions import ValidationError
from django.db import models
from django.core.files import File
from django.utils import timezone
import barcode
from barcode.writer import ImageWriter
from account.models import CustomUser


def validate_file_extension(value):
    """Faylning formatini tekshirish uchun validator."""
    if value.content_type not in ['application/pdf', 'application/msword',
                                  'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        raise ValidationError("Faqat PDF va Word formatidagi fayllarni yuklash mumkin.")


class Library(models.Model):
    name = models.CharField(max_length=255, help_text="Kutubhona nomi")
    address = models.CharField(max_length=255, help_text="Manzili")
    number = models.CharField(max_length=255, help_text="Kutubhona raqami")
    created_date = models.DateField(auto_now_add=True, help_text="Model yaratilgan sana")
    updated_date = models.DateField(auto_now=True, help_text="Model yangilangan sana")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='libraries', help_text="Kutubhona yaratgan foydalanuvchi")
    active = models.BooleanField(default=False, help_text="Kutubhona faol yoki emasligini ko'rsatadi")

    def __str__(self):
        return self.name


def generate_book_id():
    """Kitob identifikatorini avtomatik tarzda yaratish."""
    return '309' + ''.join(random.choices(string.digits, k=6))


def generate_barcode_book(book_id):
    """Kitob uchun QR kodni avtomatik tarzda yaratish."""
    CODE128 = barcode.get_barcode_class('code128')
    code128 = CODE128(book_id, writer=ImageWriter())
    buffer = BytesIO()
    code128.write(buffer)
    return buffer.getvalue()


class Book(models.Model):
    """Kitob modeli."""
    title = models.CharField(max_length=255, help_text="Kitobning sarlavhasi")
    author = models.CharField(max_length=255, help_text="Kitobning muallifi")
    quantity = models.IntegerField(default=0, help_text="Kitoblar soni")
    available_quantity = models.IntegerField(help_text="Qolgan Kitoblar soni", null=True, blank=True)
    book_id = models.CharField(max_length=9, unique=True, default=generate_book_id, help_text="Kitob identifikatori")
    barcode_book = models.ImageField(upload_to='barcode_books/', blank=True, null=True,
                                     help_text="Kitob QR kod (mavjud bo'lsa)")
    image = models.ImageField(upload_to='book_covers/', blank=True, null=True, help_text="Kitob rasmi (mavjud bo'lsa)")
    publication_year = models.IntegerField(help_text="Kitobning nashr yili")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Kitob yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, help_text="Kitob oxirgi yangilanish vaqti")
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='books', null=True, blank=True,
                                help_text="Kitob kutubxonasi")
    status = models.CharField(max_length=20, choices=[('accepted', 'Tasdiqlangan'), ('rejected', 'Tasdiqlanmagan')],
                              default='rejected', help_text="Kitob holati")
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='added_books',
                                 help_text="Kitobni qo'shgan foydalanuvchi")
    isbn = models.CharField(max_length=20, blank=True, null=True, help_text="Kitobning ISBN raqami")
    file = models.FileField(upload_to='book_files/', validators=[validate_file_extension],
                            help_text="Kitob fayli (faqat Word va PDF)")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Agar barcode_book bo'sh bo'lsa QR kodni generatsiya qilib saqlash
        if not self.barcode_book:
            image_filename = f"{self.book_id}.png"
            self.barcode_book.save(image_filename, File(BytesIO(generate_barcode_book(self.book_id))), save=False)
        if not self.barcode_book:
            image_filename = f"{self.book_id}.png"
            self.barcode_book.save(image_filename, File(BytesIO(generate_barcode_book(self.book_id))), save=False)
        return super().save(*args, **kwargs)


class BookLoan(models.Model):
    STATUS_CHOICES = [
        ('pending', 'kutilmoqda'),
        ('returned', 'qaytarilgan'),
        ('not_returned', 'qaytarilmadi'),
        ('7_days', '7 kun'),
        ('10_days', '10 kun'),
        ('15_days', '15 kun'),
        ('1_month', '1 oy'),
        ('2_months', '2 oy'),
        ('3_months', '3 oy'),
        ('4_months', '4 oy'),
        ('5_months', '5 oy'),
        ('6_months', '6 oy'),
        ('1_year', '1 yil'),
        ('2_years', '2 yil'),
    ]
    """Kitob berish modeli."""
    book = models.ForeignKey('Book', on_delete=models.CASCADE, help_text="Kitob")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, help_text="Foydalanuvchi")
    loan_date = models.DateTimeField(default=timezone.now, help_text="Kitob olingan vaqti")
    return_date = models.DateTimeField(blank=True, null=True, help_text="Kitobni qaytarilishi kerak bo'lgan vaqti")

    quantity = models.IntegerField(help_text="Kitob" , blank=True, null=True, verbose_name="Olingan kitob soni")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', help_text="Kitob holati")
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='book_loans', null=True, blank=True,help_text="Kitob beriladigan kutubxona")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Kitob berilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, help_text="Kitob oxirgi berilgan vaqti")

    def __str__(self):
        return f"{self.book} - {self.user}"

    def check_return_status(self):
        """Kitobni qaytarilganligini tekshirish va qaytarilish muddatini hisoblash."""
        if self.status != 'returned':
            loan_duration = timezone.now() - self.loan_date
            if loan_duration.days > 7:
                self.status = 'not_returned'
                self.save()
                return True
            elif self.status in ['7_days', '10_days', '15_days', '1_month', '2_months', '3_months', '4_months',
                                 '5_months', '6_months', '1_year', '2_years']:
                duration_map = {
                    '7_days': 7,
                    '10_days': 10,
                    '15_days': 15,
                    '1_month': 30,
                    '2_months': 60,
                    '3_months': 90,
                    '4_months': 120,
                    '5_months': 150,
                    '6_months': 180,
                    '1_year': 365,
                    '2_years': 730,
                }
                max_loan_duration = timedelta(days=duration_map[self.status])
                if loan_duration > max_loan_duration:
                    self.status = 'not_returned'
                    self.save()
                    return True
        return False


class AdminLibrary(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='library')
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='librarians')
    created_at = models.DateTimeField(auto_now_add=True, help_text="Kutubhonaga admin tayinlangan vaqti")
    updated_at = models.DateTimeField(auto_now=True, help_text="Kutubhonaga admin oxirgi tayinlangan vaqti")

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
    file = models.FileField(upload_to='online_books/', validators=[validate_file_extension],
                            help_text="Onlayn kitob fayli")
    created_date = models.DateTimeField(auto_now_add=True, help_text="Onlayn kitob yaratilgan vaqti")
    updated_date = models.DateTimeField(auto_now=True, help_text="Model yangilangan sana")

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
    created_date = models.DateTimeField(auto_now_add=True, help_text="Kitobga buyurtma vaqti")
    updated_date = models.DateTimeField(auto_now=True, help_text="Kitobga buyurtma oxirgi vaqti")
    def __str__(self):
        return f"{self.book_title} - {self.user}"
