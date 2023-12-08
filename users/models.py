from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    key = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='profile_image')
    profile_cover = models.ImageField(upload_to='profile_cover')
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    followers = models.ManyToManyField("self", blank=True, related_name='user_followers', symmetrical=False)
    following = models.ManyToManyField("self", blank=True, related_name='user_following', symmetrical=False)
    verified = models.BooleanField(default=False)
    bio = models.CharField(max_length=150)
    birth_of_day = models.DateField(blank=True, null=True)
    roles = models.ManyToManyField(Role, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + '/'):]

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True
