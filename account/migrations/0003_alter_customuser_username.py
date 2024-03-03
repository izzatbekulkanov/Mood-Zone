# Generated by Django 5.0.2 on 2024-03-01 17:32

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default=account.models.CustomUserManager._generate_random_username, max_length=9, unique=True),
        ),
    ]
