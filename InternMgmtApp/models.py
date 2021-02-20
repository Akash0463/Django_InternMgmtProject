from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10,default='')
    university = models.CharField(max_length=50)
    
class ApplicationDetails(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    main_stream = models.CharField(max_length=50, default='')
    field = models.CharField(max_length=50, default='')
    date  = models.DateField(auto_now=True)
    status = models.CharField(max_length=50, default='Pending')
    resume = models.FileField(upload_to='resume')