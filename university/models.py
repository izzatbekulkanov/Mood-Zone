from django.db import models



class Education(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    head = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='university_logos/')
    private_number = models.CharField(max_length=20)
    website = models.URLField()
    platform_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Departament(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    head = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    telegram_bot_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=10)
    major = models.ForeignKey('university.Major', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name