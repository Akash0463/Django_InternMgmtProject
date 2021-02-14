from django.db import models

# Create your models here.

class application_details(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    university = models.CharField(max_length=50)
    phone = models.CharField(max_length=10,null=False, blank=False, unique=True)
    applied_in = models.CharField(max_length=50, default='')
    resume = models.FileField(upload_to='resume')