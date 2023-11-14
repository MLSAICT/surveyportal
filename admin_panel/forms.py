# admin_panel/forms.py
from django import forms
from .models import Admin, Island, PSMRequestApproval, CSRRequestApproval
from django.contrib.auth.forms import AuthenticationForm
from surveyor.models import Surveyor, PSMRequest, CSRRequest

class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['username', 'password']

class IslandForm(forms.ModelForm):
    class Meta:
        model = Island
        fields = ['code', 'name']

class PSMRequestApprovalForm(forms.ModelForm):
    class Meta:
        model = PSMRequestApproval
        fields = ['admin', 'psm_request']

class CSRRequestApprovalForm(forms.ModelForm):
    class Meta:
        model = CSRRequestApproval
        fields = ['admin', 'csr_request']
        
class SurveyorForm(forms.ModelForm):
    class Meta:
        model = Surveyor
        fields = ['license_number', 'name', 'password']  # Add other fields as needed

class PSMRequestSelectionForm(forms.Form):
    psm_request = forms.ModelChoiceField(
        queryset=PSMRequest.objects.all(),
        label='Select a PSM Request',
        empty_label=None  # Disables the empty label in the dropdown
    )

class CSRRequestSelectionForm(forms.Form):
    psm_request = forms.ModelChoiceField(
        queryset=CSRRequest.objects.all(),
        label='Select a PSM Request',
        empty_label=None  # Disables the empty label in the dropdown
    )
