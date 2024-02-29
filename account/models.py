from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
import random
import string


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _generate_random_username(self):
        """Generate a random 9-digit number."""
        random_number = ''.join(random.choices(string.digits, k=12))
        return '309' + random_number  # Adding '309' as prefix

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
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





class CustomUser(AbstractUser):
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

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=9, default=CustomUserManager()._generate_random_username, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    full_name = models.CharField(max_length=181, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(max_length=20, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    password_save = models.CharField(_('password save'), max_length=128)  # Added password_save field
    user_role = models.CharField(max_length=20, choices=user_role_choices, default='simple', null=True, blank=True)

    # Additional fields for the university
    passport_serial = models.CharField(max_length=20, null=True, blank=True)
    passport_issue_date = models.DateField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)


    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

    USERNAME_FIELD = 'email'  # Foydalanuvchilar email orqali login qila oladilar
    REQUIRED_FIELDS = ['username']  # username kerakli maydon


