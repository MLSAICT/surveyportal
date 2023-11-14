# admin_panel/auth_backends.py
from django.contrib.auth.backends import ModelBackend
from .models import Admin

class AdminBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            admin = Admin.objects.get(username=username)
        except Admin.DoesNotExist:
            return None

        if admin.check_password(password):
            return admin
        return None
