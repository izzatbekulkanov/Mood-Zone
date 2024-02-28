from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    NEWS_CHOICES = [
        ('breaking', 'Breaking News'),
        ('sports', 'Sports News'),
        ('entertainment', 'Entertainment News'),
        ('politics', 'Politics News'),
        ('technology', 'Technology News'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    main_info = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True, blank=True)
    news_type = models.CharField(max_length=20, choices=NEWS_CHOICES, default='other')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
