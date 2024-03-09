# Generated by Django 5.0.2 on 2024-03-09 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Fakultet nomi')),
                ('code', models.CharField(max_length=20, verbose_name='Fakultet kodi')),
                ('parent', models.CharField(blank=True, max_length=20, null=True, verbose_name='Boshqa fakultet')),
                ('active', models.BooleanField(default=True, verbose_name='Faol')),
                ('structure_type', models.CharField(choices=[('10', 'Boshqa'), ('11', 'Fakultet'), ('12', 'Kafedra'), ('13', 'Bo‘lim'), ('14', 'Boshqarma'), ('15', 'Markaz'), ('16', 'Rektorat')], max_length=2, verbose_name='Bo‘lim turi')),
            ],
        ),
        migrations.CreateModel(
            name='EducationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name="Ta'lim shakli kodi")),
                ('name', models.CharField(max_length=255, verbose_name="Ta'lim shakli nomi")),
            ],
        ),
        migrations.CreateModel(
            name='EducationLang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name="Ta'lim tili kodi")),
                ('name', models.CharField(max_length=255, verbose_name="Ta'lim tili nomi")),
            ],
        ),
        migrations.CreateModel(
            name='EducationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name="Ta'lim turi kodi")),
                ('name', models.CharField(max_length=255, verbose_name="Ta'lim turi nomi")),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Bosqich kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Bosqich nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Semestr kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Semestr nomi')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_load', models.IntegerField(verbose_name='Akademik yuk')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name="Ta'lim turi kodi")),
                ('name', models.CharField(max_length=255, verbose_name="Ta'lim turi nomi")),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Universitet kodi')),
                ('name', models.CharField(max_length=255, verbose_name='Universitet nomi')),
                ('api_url', models.URLField(blank=True, null=True, verbose_name='API URL')),
                ('student_url', models.URLField(blank=True, null=True, verbose_name='Student URL')),
                ('employee_url', models.URLField(blank=True, null=True, verbose_name='Xodimlar URL')),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name="O'quv reja kodi")),
                ('name', models.CharField(max_length=255, verbose_name='Dastur nomi')),
                ('semester_count', models.IntegerField(blank=True, null=True, verbose_name='Semestrlar soni')),
                ('education_period', models.IntegerField(blank=True, null=True, verbose_name="Ta'lim davomi (Yilda)")),
                ('educationForm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.educationform', verbose_name="Ta'lim shakli")),
                ('educationType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.educationtype', verbose_name="Ta'lim turi")),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Yo'nalish nomi")),
                ('code', models.CharField(max_length=20, verbose_name="Yo'nalish kodi")),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.department')),
                ('educationType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.educationtype', verbose_name="Ta'lim turi")),
            ],
        ),
        migrations.CreateModel(
            name='GroupUniver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Guruh nomi')),
                ('code', models.CharField(max_length=20, verbose_name='Guruh kodi')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.curriculum', verbose_name="O'quv rejasi")),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.department', verbose_name='Fakultet')),
                ('educationLang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.educationlang', verbose_name="Ta'lim tili")),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.specialty', verbose_name='Mutaxassislik')),
            ],
        ),
        migrations.AddField(
            model_name='curriculum',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.specialty', verbose_name="Yo'nalish"),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_acload', models.IntegerField(verbose_name='Umumiy akademik yuk')),
                ('credit', models.IntegerField(blank=True, null=True, verbose_name='Kredit')),
                ('resource_count', models.IntegerField(blank=True, null=True, verbose_name='Resurslar soni')),
                ('in_group', models.IntegerField(blank=True, null=True, verbose_name='Guruhda')),
                ('at_semester', models.BooleanField(blank=True, default=True, null=True, verbose_name='Semestrda')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.department', verbose_name="Bo'lim")),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.semester', verbose_name='Semestr')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_fan', to='university.subject', verbose_name='Fan')),
                ('subjectDetails', models.ManyToManyField(to='university.subjectdetail', verbose_name='Fan tafsilotlari')),
            ],
        ),
        migrations.AddField(
            model_name='subjectdetail',
            name='trainingType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.trainingtype', verbose_name="Ta'lim turi"),
        ),
    ]
