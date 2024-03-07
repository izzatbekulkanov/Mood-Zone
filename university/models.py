from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import random
import string


class University(models.Model):
    code = models.CharField(max_length=20, verbose_name="Universitet kodi")
    name = models.CharField(max_length=255, verbose_name="Universitet nomi")

    def __str__(self):
        return self.name


class Department(models.Model):
    # structureType turining variantlari
    BOSHQA = '10'
    MAHALLIY = '11'
    KAFEDRA = '12'
    BOLIM = '13'
    BOSHQARMA = '14'
    MARKAZ = '15'
    REKTORAT = '16'

    STRUCTURE_TYPE_CHOICES = [
        (BOSHQA, 'Boshqa'),
        (MAHALLIY, 'Mahalliy'),
        (KAFEDRA, 'Kafedra'),
        (BOLIM, 'Bo‘lim'),
        (BOSHQARMA, 'Boshqarma'),
        (MARKAZ, 'Markaz'),
        (REKTORAT, 'Rektorat'),
    ]


    name = models.CharField(max_length=255, verbose_name="Fakultet nomi")
    code = models.CharField(max_length=20, verbose_name="Fakultet kodi")
    parent = models.CharField(max_length=20, null=True, blank=True, verbose_name="Boshqa fakultet")
    active = models.BooleanField(default=True, verbose_name="Faol")
    structure_type = models.CharField(
        max_length=2,
        choices=STRUCTURE_TYPE_CHOICES,
        verbose_name='Bo‘lim turi'
    )

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=255, verbose_name="Yo'nalish nomi")
    code = models.CharField(max_length=20, verbose_name="Yo'nalish kodi")

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name="Guruh nomi")
    educationLang = models.ForeignKey('EducationLang', on_delete=models.CASCADE, verbose_name="Ta'lim tili")

    def __str__(self):
        return self.name


class EducationLang(models.Model):
    code = models.CharField(max_length=20, verbose_name="Ta'lim tili kodi")
    name = models.CharField(max_length=255, verbose_name="Ta'lim tili nomi")

    def __str__(self):
        return self.name


class Semester(models.Model):
    code = models.CharField(max_length=20, verbose_name="Semestr kodi")
    name = models.CharField(max_length=255, verbose_name="Semestr nomi")

    def __str__(self):
        return self.name


class Level(models.Model):
    code = models.CharField(max_length=20, verbose_name="Bosqich kodi")
    name = models.CharField(max_length=255, verbose_name="Bosqich nomi")

    def __str__(self):
        return self.name


class EducationForm(models.Model):
    code = models.CharField(max_length=20, verbose_name="Ta'lim shakli kodi")
    name = models.CharField(max_length=255, verbose_name="Ta'lim shakli nomi")

    def __str__(self):
        return self.name


class EducationType(models.Model):
    code = models.CharField(max_length=20, verbose_name="Ta'lim turi kodi")
    name = models.CharField(max_length=255, verbose_name="Ta'lim turi nomi")

    def __str__(self):
        return self.name


class Curriculum(models.Model):
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, verbose_name="Yo'nalish")
    educationType = models.ForeignKey('EducationType', on_delete=models.CASCADE, verbose_name="Ta'lim turi")
    educationForm = models.ForeignKey('EducationForm', on_delete=models.CASCADE, verbose_name="Ta'lim shakli")
    name = models.CharField(max_length=255, verbose_name="Dastur nomi")
    semester_count = models.IntegerField(verbose_name="Semestrlar soni")
    education_period = models.IntegerField(verbose_name="Ta'lim davomi")

    def __str__(self):
        return self.name


class SubjectDetail(models.Model):
    trainingType = models.ForeignKey('TrainingType', on_delete=models.CASCADE, verbose_name="Ta'lim turi")
    academic_load = models.IntegerField(verbose_name="Akademik yuk")

    def __str__(self):
        return f"{self.trainingType.name} - {self.academic_load}"


class TrainingType(models.Model):
    code = models.CharField(max_length=20, verbose_name="Ta'lim turi kodi")
    name = models.CharField(max_length=255, verbose_name="Ta'lim turi nomi")

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, verbose_name="Fan", related_name="subject_fan")
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE, verbose_name="Semestr")
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name="Bo'lim")
    subjectDetails = models.ManyToManyField('SubjectDetail', verbose_name="Fan tafsilotlari")
    total_acload = models.IntegerField(verbose_name="Umumiy akademik yuk")
    credit = models.IntegerField(verbose_name="Kredit")
    resource_count = models.IntegerField(verbose_name="Resurslar soni")
    in_group = models.IntegerField(verbose_name="Guruhda")
    at_semester = models.BooleanField(default=True, verbose_name="Semestrda")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    def __str__(self):
        return f"{self.subject.name} - {self.semester.name}"
