# Generated by Django 5.0.3 on 2024-03-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_author_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, help_text="Kitob muallifining rasmi (mavjud bo'lsa)", null=True, upload_to='author_image/'),
        ),
    ]
