from django.db import models
from user.models import PSMRequest

# Create your models here.
class Admin_users(models.Model):
    name = models.CharField(max_length=255, null =True)
    password = models.CharField(max_length=255, null =True)

class UpdateLog(models.Model):
    psm_request = models.ForeignKey(PSMRequest, on_delete=models.CASCADE)
    date = models.DateField()
    staff = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    comment = models.TextField()