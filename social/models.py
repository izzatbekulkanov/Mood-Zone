from django.db import models
from users.models import CustomUser
# Create your models here.
ACTION_CHOICES = (
    ('like', "Like"),
    ('saved', "Saved"),
    ('view', "View")
)


class Post(models.Model):
    repost = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    media = models.FileField(upload_to="post_media/")
    likes = models.PositiveIntegerField(default=0)
    saveds = models.PositiveIntegerField(default=0)
    reposts = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body


class Action(models.Model):
    action_type = models.CharField(max_length=25, choices=ACTION_CHOICES)
    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_actions')
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_actions')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.action_type)


class Notification(models.Model):
    body = models.CharField(max_length=300)
    datetime = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.body)

