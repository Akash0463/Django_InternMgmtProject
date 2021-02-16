from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10,default='')
    university = models.CharField(max_length=50)
    
class ApplicationDetails(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    applied_in = models.CharField(max_length=50, default='')
    resume = models.FileField(upload_to='resume')