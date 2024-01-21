# admin_panel/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class AdminUserManager(models.Manager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')

        if password:
            extra_fields['password'] = make_password(password)

        user = self.model(username=username, **extra_fields)
        user.save(using=self._db)
        return user


class Admin(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    objects = AdminUserManager()

    def __str__(self):
        return self.username

class Island(models.Model):
    code = models.CharField(max_length=254, unique=True)
    atoll = models.CharField(max_length=255, null = True)
    name = models.CharField(max_length=255)

def __str__(self):
        return f"{self.code} - {self.atoll} - {self.name}"

class PSMRequestApproval(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    psm_request = models.ForeignKey('surveyor.PSMRequest', on_delete=models.CASCADE)
    approved_at = models.DateTimeField(auto_now_add=True)

class CSRRequestApproval(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    csr_request = models.ForeignKey('surveyor.CSRRequest', on_delete=models.CASCADE)
    approved_at = models.DateTimeField(auto_now_add=True)
