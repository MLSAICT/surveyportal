from django.db import models


def get_default_comment_file():
    return 'default_file.pdf'

class Surveyors(models.Model):
    license_number = models.CharField(max_length=255, null =True)
    name = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Set the field for username, which will be used for authentication (must be unique)
    USERNAME_FIELD = 'license_number'

    def __str__(self):
        return self.license_number



class ReferenceLetterPSM(models.Model):
    document = models.FileField(upload_to='ReferenceLetterPSM/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class RequestLetterPSM(models.Model):
    document1 = models.FileField(upload_to='RequestLetterPSM/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class PSMRequest(models.Model):
    surveyor_name = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=False)
    date_applied = models.DateField(null= True)
    expiry = models.DateField(null=True)
    psm_number = models.CharField(max_length= 255,null=True)
    comment = models.FileField(upload_to='commentPSM/', default=get_default_comment_file)

    island = models.ForeignKey('Islands', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.island.island_name} ({self.island.island_code})"

class Islands(models.Model):
    atoll = models.CharField(max_length=100, null=True)
    island_code = models.CharField(max_length=100, null=True)
    island_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.island_name} ({self.island_code})"
    
    

   