# surveyor/models.py
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class Surveyor(models.Model):
    license_number = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    # Add other fields...

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.license_number
    
  

   

class PSMRequest(models.Model):
    surveyor = models.ForeignKey(Surveyor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    island = models.CharField(max_length=255)
    request_letter = models.FileField(upload_to='psm_requests/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

class CSRRequest(models.Model):
    psm_request = models.ForeignKey(PSMRequest, on_delete=models.CASCADE)
    surveyor = models.ForeignKey(Surveyor, on_delete=models.CASCADE)
    excel_data = models.FileField(upload_to='csr_requests/excel/')
    raw_data = models.FileField(upload_to='csr_requests/raw_data/')
    survey_report = models.FileField(upload_to='csr_requests/reports/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
