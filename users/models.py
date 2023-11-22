from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # Customizing fields
    profile_picture = models.ImageField(
        upload_to='media/profile_pics/',
        null=True,
        blank=True,
        default='assets/images/avatars/default-user.png'
    )
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return self.username
