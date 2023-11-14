# survey_portal/surveyor/urls.py
from django.urls import path
from .views import surveyor_dashboard, submit_psm_request, submit_csr_request, custom_login
from django.conf import settings
from django.conf.urls.static import static
app_name = 'surveyor'

urlpatterns = [
    path('dashboard/', surveyor_dashboard, name='surveyor_dashboard'),
    path('submit_psm_request/', submit_psm_request, name='submit_psm_request'),
    path('submit_csr_request/', submit_csr_request, name='submit_csr_request'),
    path('login/', custom_login, name='custom_login'),
    # Add more paths as needed
]

