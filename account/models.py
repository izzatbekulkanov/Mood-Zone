from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import random
import string
from django.utils.translation import gettext_lazy as _

from django.utils import timezone

from university.models import University, Specialty, Group, Department, EducationType, EducationForm, Curriculum


class CustomUserManager(BaseUserManager):
    """Define a model manager for CustomUser model with no username field."""

    def _generate_random_username(self):
        """Generate a random 9-digit number."""
        random_number = ''.join(random.choices(string.digits, k=12))
        return '309' + random_number  # Adding '309' as prefix

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a CustomUser with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, role=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('username', self._generate_random_username())
        if role:
            extra_fields.setdefault('role', role)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Gender(models.Model):
    code = models.CharField(max_length=20, verbose_name="Jins kodi")
    name = models.CharField(max_length=255, verbose_name="Jins nomi")

    def __str__(self):
        return self.name

class EmployeeStatus(models.Model):
    code = models.CharField(max_length=20, verbose_name="Xodim holati kodi")
    name = models.CharField(max_length=255, verbose_name="Xodim holati nomi")

    def __str__(self):
        return self.name


class EmployeeType(models.Model):
    code = models.CharField(max_length=20, verbose_name="Xodim turi kodi")
    name = models.CharField(max_length=255, verbose_name="Xodim turi nomi")

    def __str__(self):
        return self.name


class Country(models.Model):
    code = models.CharField(max_length=20, verbose_name="Mamlakat kodi")
    name = models.CharField(max_length=255, verbose_name="Mamlakat nomi")

    def __str__(self):
        return self.name


class Province(models.Model):
    code = models.CharField(max_length=20, verbose_name="Viloyat kodi")
    name = models.CharField(max_length=255, verbose_name="Viloyat nomi")

    def __str__(self):
        return self.name


class District(models.Model):
    code = models.CharField(max_length=20, verbose_name="Tuman kodi")
    name = models.CharField(max_length=255, verbose_name="Tuman nomi")

    def __str__(self):
        return self.name


class Citizenship(models.Model):
    code = models.CharField(max_length=20, verbose_name="Fuqarolik kodi")
    name = models.CharField(max_length=255, verbose_name="Fuqarolik nomi")

    def __str__(self):
        return self.name


class StudentType(models.Model):
    code = models.CharField(max_length=20, verbose_name="Talaba turi kodi")
    name = models.CharField(max_length=255, verbose_name="Talaba turi nomi")

    def __str__(self):
        return self.name

class StudentStatus(models.Model):
    code = models.CharField(max_length=20, verbose_name="Talabaning holati kodi")
    name = models.CharField(max_length=255, verbose_name="Talabaning holati nomi")

    def __str__(self):
        return self.name
class CustomUser(AbstractUser):
    type_choice = (
        ("1", "Hodim"),
        ("2", "Talaba"),
    )
    user_role_choices = [
        ('dean', 'Dekan'),
        ('head', 'Boshqaruvchi'),
        ('rector', 'Rektor'),
        ('simple', 'Oddiy'),
        ('admin', 'Administrator'),
        ('student', 'Student'),
        ('employee', 'Xodim'),
        ('book_subscriber', 'Kitob Obunachisi'),
        ('librarian', 'Kutubxonachi'),
        ('examiner', 'Imtihon Topshiruvchi'),
    ]
    full_name = models.CharField(null=True, blank=True, max_length=255, verbose_name="To'liq ism")
    short_name = models.CharField(null=True, blank=True, max_length=255, verbose_name="Qisqa ism")
    first_name = models.CharField(null=True, blank=True, max_length=255, verbose_name="Birinchi ism")
    second_name = models.CharField(null=True, blank=True, max_length=255, verbose_name="Ikkinchi ism")
    third_name = models.CharField(null=True, blank=True, max_length=255, verbose_name="Uchinchi ism")
    username = models.CharField(null=True, blank=True, max_length=9, unique=True)
    email = models.EmailField(('email address'), unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(null=True, max_length=15, blank=True)
    password_save = models.CharField(('password save'), max_length=128)  # Added password_save field
    image = models.CharField(blank=True, null=True,max_length=255, verbose_name="Rasm")
    year_of_enter = models.CharField(null=True, blank=True, max_length=255, verbose_name="Kirish yili")
    employee_id_number = models.IntegerField(blank=True, null=True, verbose_name="Xodim raqami")
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name="Jins", blank=True, null=True,)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Fakultet", blank=True, null=True,)
    employeeStatus = models.ForeignKey(EmployeeStatus, on_delete=models.CASCADE, verbose_name="Xodimholati", blank=True, null=True)
    user_type = models.CharField(_('Turi'), choices=type_choice, default="1", max_length=20, blank=True, null=True)
    employeeType = models.ForeignKey(EmployeeType, on_delete=models.CASCADE, verbose_name="Xodim turi", blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name="Tug'ilgan kun")
    is_student = models.BooleanField(default=False, verbose_name="Talaba")
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name="Universitet", null=True, blank=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name="Mutaxassislik", null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Guruh", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Davlat", null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="Viloyat", null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name="Tuman", null=True, blank=True)
    citizenship = models.ForeignKey(Citizenship, on_delete=models.CASCADE, verbose_name="Fuqarolik", null=True, blank=True)
    educationForm = models.ForeignKey(EducationForm, on_delete=models.CASCADE, verbose_name="Ta'lim shakli", null=True, blank=True)
    educationType = models.ForeignKey(EducationType, on_delete=models.CASCADE, verbose_name="Ta'lim turi", null=True, blank=True)
    studentType = models.ForeignKey(StudentType, on_delete=models.CASCADE, verbose_name="Talaba turi", null=True, blank=True)
    studentStatus = models.ForeignKey(StudentStatus, on_delete=models.CASCADE, verbose_name="Talaba holati", null=True, blank=True)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, verbose_name="O'quv rejasi", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")
    last_login = models.DateTimeField(default=timezone.now)
    last_activity = models.DateTimeField(null=True, blank=True)
    hash = models.CharField(null=True, blank=True, max_length=255, verbose_name="Hash")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_role = models.CharField(max_length=20, choices=user_role_choices, default='simple', null=True, blank=True)

    # Additional fields for the university
    passport_serial = models.CharField(max_length=20, null=True, blank=True)
    passport_issue_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.username  # yoki return self.email yoki return self.full_name

    USERNAME_FIELD = 'email'  # Users login in with their email
    REQUIRED_FIELDS = ['username']  # username required field



