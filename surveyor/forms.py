# surveyor/forms.py
from django import forms
from .models import PSMRequest, CSRRequest, Surveyor
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from admin_panel.models import Island

class SurveyorLoginForm(forms.Form):
    license_number = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # def clean(self):
    #     cleaned_data = super().clean()
    #     license_number = cleaned_data.get('license_number')
    #     password = cleaned_data.get('password')

    #     # Validate the license_number and password
    #     if license_number and password:
    #         surveyor = Surveyor.objects.filter(license_number=license_number).first()
    #         if surveyor and check_password(password, surveyor.password):
    #             # Successfully authenticated
    #             return cleaned_data
    #         else:
    #             self.add_error('password', 'Invalid password')
    #     elif license_number:
    #         # If no password provided, assume it's for authentication only
    #         self.add_error('password', 'Password is required for login')

    #     return cleaned_data
    
    
class PSMRequestForm(forms.ModelForm):
    # Add a field for the Island model
    island = forms.ModelChoiceField(
        queryset=Island.objects.all(),
        empty_label="Select an island",
        to_field_name='id',
    )

    class Meta:
        model = PSMRequest
        fields = ['name', 'island', 'request_letter'] 

class CSRRequestForm(forms.ModelForm):
    class Meta:
        model = CSRRequest
        fields = ['psm_request', 'excel_data', 'raw_data', 'survey_report']

