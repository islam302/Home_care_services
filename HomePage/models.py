from django.db import models
from django.contrib.auth import settings

# Create your models here.


class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='nurse')
    bio = models.TextField(max_length=1000, null=True, blank=True)
    national_id = models.ImageField(upload_to='national_id_photo/', null=True, blank=True)
    resume = models.FileField(upload_to='resume/', null=True, blank=True)
    employee_photo = models.ImageField(upload_to='employee_photo/', null=True, blank=True)


class Services(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('quick_services', 'حالات طارئة'),
        ('elderly_care', 'رعاية الاطفال'),
        ('clinical_care', 'الرعاية السريرية'),
        ('disabled_care', 'رعاية المعاقين'),
        ('child_care', 'رعاية الطفل'),
        ('wound_care', 'رعاية المصابين'),
    ]

    service_name = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client')
    client_photo = models.ImageField(upload_to='client_photos/', null=True, blank=True)
    national_id = models.ImageField(upload_to='clients_national_id_photos/', null=True, blank=True)
    current_location = models.CharField(max_length=255)
    service_needed = models.ForeignKey(Services, on_delete=models.PROTECT, related_name='service_needed')

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        self._meta.get_field('service_needed').choices = self.get_service_choices()

    def get_service_choices(self):
        return [(service.id, service.service_name) for service in Services.objects.all()]


class ContactUs(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=15, unique=True)
    message = models.TextField(max_length=1000)


class Jobs(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
    ]

    job_title = models.CharField(max_length=250)
    salary = models.DecimalField(max_digits=20, decimal_places=2)
    experience_needed = models.IntegerField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)


class JobSeekers(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_seekers')
    job_title = models.CharField(max_length=250)


class CustomerReviews(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    review = models.TextField()
