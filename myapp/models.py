from django.db import models

# Create your models here.
PROVINCE_CHOICE= (
    ('Pro 1', 'Pro 1'),
    ('Pro 2', 'Pro 2'),
    ('Pro 3', 'Pro 3'),
    ('Pro 4', 'Pro 4'),
    ('Pro 5', 'Pro 5'),
    ('Pro 6', 'Pro 6'),
    ('Pro 7', 'Pro 7'),
)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin = models.PositiveIntegerField()
    provinces = models.CharField(choices=PROVINCE_CHOICE, max_length=100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)

