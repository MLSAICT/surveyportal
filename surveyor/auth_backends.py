# surveyor/auth_backends.py
from django.contrib.auth.backends import ModelBackend
from .models import Surveyor

from django.contrib.auth import get_user_model

class SurveyorBackend(ModelBackend):
    def authenticate(self, request, license_number=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(license_number=license_number)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
