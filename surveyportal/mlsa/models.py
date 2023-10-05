from django.db import models

# Create your models here.
class Admin_users(models.Model):
    name = models.CharField(max_length=255, null =True)
    password = models.CharField(max_length=255, null =True)

