from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_image')
    profile_cover = models.ImageField(upload_to='profile_cover')
    followers = models.ManyToManyField("self", blank=True, related_name='user_followers', symmetrical=False)
    following = models.ManyToManyField("self", blank=True, related_name='user_following', symmetrical=False)
    verified = models.BooleanField(default=False)
    bio = models.CharField(max_length=150)
    birth_of_day = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

