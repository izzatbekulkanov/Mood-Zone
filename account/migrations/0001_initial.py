# Generated by Django 5.0.3 on 2024-03-21 01:00

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('university', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Talabaning turar joyi kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Talabaning turar joyi nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Citizenship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Fuqarolik kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Fuqarolik nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Mamlakat kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Mamlakat nomi')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Tuman kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Tuman nomi')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Xodim holati kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Xodim holati nomi')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Xodim turi kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Xodim turi nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Jins kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Jins nomi')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name="To'lov turi")),
                ('name', models.CharField(max_length=255, verbose_name="To'lov nomi")),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Viloyat kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Viloyat nomi')),
            ],
        ),
        migrations.CreateModel(
            name='StaffPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name="Xodim o'rni kodi")),
                ('name', models.CharField(max_length=255, verbose_name="Xodim o'rni nomi")),
            ],
        ),
        migrations.CreateModel(
            name='StudentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Talabaning holati kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Talabaning holati nomi')),
            ],
        ),
        migrations.CreateModel(
            name='StudentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Talaba turi kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Talaba turi nomi')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name="To'liq ism")),
                ('short_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Qisqa ism')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ism')),
                ('second_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Familia')),
                ('third_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Otasining ismi')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name="Tug'ilgan kun")),
                ('student_id_number', models.IntegerField(blank=True, null=True, verbose_name='Talaba raqami')),
                ('image', models.URLField(blank=True, max_length=255, null=True, verbose_name='Rasm')),
                ('imageFile', models.ImageField(blank=True, null=True, upload_to='students/%Y/%m/%d', verbose_name='Rasmi faylda')),
                ('year_of_enter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Kirish yili')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")),
                ('hash', models.CharField(blank=True, max_length=255, null=True, verbose_name='Hash')),
                ('username', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('password_save', models.CharField(blank=True, max_length=128, null=True, verbose_name='password save')),
                ('employee_id_number', models.IntegerField(blank=True, null=True, verbose_name='Xodim raqami')),
                ('contractDate', models.CharField(blank=True, max_length=255, null=True, verbose_name='Shartnoma sanasi')),
                ('user_type', models.CharField(blank=True, choices=[('1', 'Talaba'), ('2', 'Hodim')], default='1', max_length=20, null=True, verbose_name='Turi')),
                ('is_student', models.BooleanField(default=False, verbose_name='Talaba')),
                ('is_followers_book', models.BooleanField(default=False, verbose_name='is_followers_book')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_activity', models.DateTimeField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('token', models.TextField(blank=True, null=True, unique=True)),
                ('passport_serial', models.CharField(blank=True, max_length=20, null=True)),
                ('passport_issue_date', models.DateField(blank=True, null=True)),
                ('full_id', models.CharField(blank=True, max_length=255, null=True, verbose_name="To'liq ID")),
                ('curriculum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.curriculum', verbose_name="O'quv rejasi")),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.department', verbose_name='Fakultet')),
                ('educationForm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.educationform', verbose_name="Ta'lim shakli")),
                ('educationType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.educationtype', verbose_name="Ta'lim turi")),
                ('educationYear', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.educationyear', verbose_name="O'quv yili")),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.groupuniver', verbose_name='Guruh')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.level', verbose_name='Bosqich')),
                ('semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.semester', verbose_name='Semestr')),
                ('specialty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.specialty', verbose_name='Mutaxassislik')),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.university', verbose_name='Universitet')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('accommodation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.accommodation', verbose_name='Turar joyi')),
                ('citizenship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.citizenship', verbose_name='Fuqarolik')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.country', verbose_name='Davlat')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.district', verbose_name='Tuman')),
                ('employeeStatus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.employeestatus', verbose_name='Xodimholati')),
                ('employeeType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.employeetype', verbose_name='Xodim turi')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.gender', verbose_name='Jins')),
                ('paymentForm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.paymentform', verbose_name="To'lov turi")),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.province', verbose_name='Viloyat')),
                ('staffPosition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffposition', to='account.staffposition', verbose_name="Xodimo'rni")),
                ('studentStatus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.studentstatus', verbose_name='Talaba holati')),
                ('studentType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.studenttype', verbose_name='Talaba turi')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
