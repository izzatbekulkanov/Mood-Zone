# Generated by Django 5.0.3 on 2024-03-21 01:00

import django.db.models.deletion
import django.utils.timezone
import library.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online_book_id', models.CharField(default=library.models.generate_book_id, help_text='Onlayn kitob identifikatori', max_length=9, unique=True)),
                ('name', models.CharField(help_text='Onlayn kitob nomi', max_length=255)),
                ('content', models.TextField(help_text='Onlayn kitob mazmuni')),
                ('file', models.FileField(help_text='Onlayn kitob fayli', upload_to='online_books/', validators=[library.models.validate_file_extension])),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Onlayn kitob yaratilgan vaqti')),
                ('updated_date', models.DateTimeField(auto_now=True, help_text='Model yangilangan sana')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Kitobning sarlavhasi', max_length=255)),
                ('author', models.CharField(help_text='Kitobning muallifi', max_length=255)),
                ('quantity', models.IntegerField(default=0, help_text='Kitoblar soni')),
                ('available_quantity', models.IntegerField(blank=True, help_text='Qolgan Kitoblar soni', null=True)),
                ('book_id', models.CharField(default=library.models.generate_book_id, help_text='Kitob identifikatori', max_length=9, unique=True)),
                ('barcode_book', models.ImageField(blank=True, help_text="Kitob QR kod (mavjud bo'lsa)", null=True, upload_to='barcode_books/')),
                ('image', models.ImageField(blank=True, help_text="Kitob rasmi (mavjud bo'lsa)", null=True, upload_to='book_covers/')),
                ('publication_year', models.IntegerField(help_text='Kitobning nashr yili')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Kitob yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Kitob oxirgi yangilanish vaqti')),
                ('status', models.CharField(choices=[('accepted', 'Tasdiqlangan'), ('rejected', 'Tasdiqlanmagan')], default='rejected', help_text='Kitob holati', max_length=20)),
                ('isbn', models.CharField(blank=True, help_text='Kitobning ISBN raqami', max_length=20, null=True)),
                ('file', models.FileField(help_text='Kitob fayli (faqat Word va PDF)', upload_to='book_files/', validators=[library.models.validate_file_extension])),
                ('added_by', models.ForeignKey(help_text="Kitobni qo'shgan foydalanuvchi", on_delete=django.db.models.deletion.CASCADE, related_name='added_books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Kutilmoqda'), ('approved', 'Tasdiqlangan'), ('canceled', "To'xtatilgan")], default='pending', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Kitobga buyurtma vaqti')),
                ('updated_date', models.DateTimeField(auto_now=True, help_text='Kitobga buyurtma oxirgi vaqti')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kutubhona nomi', max_length=255)),
                ('address', models.CharField(help_text='Manzili', max_length=255)),
                ('number', models.CharField(help_text='Kutubhona raqami', max_length=255)),
                ('created_date', models.DateField(auto_now_add=True, help_text='Model yaratilgan sana')),
                ('updated_date', models.DateField(auto_now=True, help_text='Model yangilangan sana')),
                ('active', models.BooleanField(default=False, help_text="Kutubhona faol yoki emasligini ko'rsatadi")),
                ('user', models.ForeignKey(help_text='Kutubhona yaratgan foydalanuvchi', on_delete=django.db.models.deletion.CASCADE, related_name='libraries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Kitob olingan vaqti')),
                ('return_date', models.DateTimeField(blank=True, help_text="Kitobni qaytarilishi kerak bo'lgan vaqti", null=True)),
                ('quantity', models.IntegerField(blank=True, help_text='Kitob', null=True, verbose_name='Olingan kitob soni')),
                ('status', models.CharField(choices=[('pending', 'kutilmoqda'), ('returned', 'qaytarilgan'), ('not_returned', 'qaytarilmadi'), ('7_days', '7 kun'), ('10_days', '10 kun'), ('15_days', '15 kun'), ('1_month', '1 oy'), ('2_months', '2 oy'), ('3_months', '3 oy'), ('4_months', '4 oy'), ('5_months', '5 oy'), ('6_months', '6 oy'), ('1_year', '1 yil'), ('2_years', '2 yil')], default='pending', help_text='Kitob holati', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Kitob berilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Kitob oxirgi berilgan vaqti')),
                ('book', models.ForeignKey(help_text='Kitob', on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('user', models.ForeignKey(help_text='Foydalanuvchi', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('library', models.ForeignKey(blank=True, help_text='Kitob beriladigan kutubxona', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_loans', to='library.library')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ForeignKey(blank=True, help_text='Kitob kutubxonasi', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.library'),
        ),
        migrations.CreateModel(
            name='AdminLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Kutubhonaga admin tayinlangan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Kutubhonaga admin oxirgi tayinlangan vaqti')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='library', to=settings.AUTH_USER_MODEL)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='librarians', to='library.library')),
            ],
        ),
    ]
