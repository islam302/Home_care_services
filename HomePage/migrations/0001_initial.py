# Generated by Django 5.0.3 on 2024-03-22 21:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=250)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=20)),
                ('experience_needed', models.IntegerField()),
                ('job_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(choices=[('quick_services', 'حالات طارئة'), ('elderly_care', 'رعاية الاطفال'), ('clinical_care', 'الرعاية السريرية'), ('disabled_care', 'رعاية المعاقين'), ('child_care', 'رعاية الطفل'), ('wound_care', 'رعاية المصابين')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('national_id', models.ImageField(blank=True, null=True, upload_to='national_id_photo/')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('employee_photo', models.ImageField(blank=True, null=True, upload_to='employee_photo/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nurse', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeekers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job_seekers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_photo', models.ImageField(blank=True, null=True, upload_to='client_photos/')),
                ('national_id', models.ImageField(blank=True, null=True, upload_to='clients_national_id_photos/')),
                ('current_location', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
                ('service_needed', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_needed', to='HomePage.services')),
            ],
        ),
    ]
