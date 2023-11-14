# survey_portal/admin_panel/urls.py
from django.urls import path
from .views import manage_surveyors, manage_psms, manage_csrs, approve_psm_request, approve_csr_request, admin_login, admin_dashboard, edit_surveyor, create_surveyor

app_name = 'admin_panel'

urlpatterns = [
    path('manage_surveyors/', manage_surveyors, name='manage_surveyors'),
    path('manage_psms/', manage_psms, name='manage_psms'),
    path('manage_csrs/', manage_csrs, name='manage_csrs'),
    path('approve_psm_request/', approve_psm_request, name='approve_psm_request'),
    path('approve_csr_request/', approve_csr_request, name='approve_csr_request'),
    path('login/', admin_login, name='admin_login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('edit_surveyor/<int:surveyor_id>/', edit_surveyor, name='edit_surveyor'),
    path('create_surveyor/', create_surveyor, name='create_surveyor'),  # New pattern for creating surveyors
    # Add more paths as needed
]
