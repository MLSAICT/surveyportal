# admin_panel/views.py
from django.shortcuts import render, redirect
from surveyor.models import Surveyor, PSMRequest, CSRRequest
from .models import Admin, Island, PSMRequestApproval, CSRRequestApproval
from .forms import AdminForm, IslandForm, PSMRequestApprovalForm, CSRRequestApprovalForm, SurveyorForm, PSMRequestSelectionForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest, HttpRequest
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AdminLoginForm

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                # Retrieve the user from the database
                user = Admin.objects.get(username=username)

                # Check the password
                if check_password(password, user.password):
                    # Password is correct, log in the user
                    # You can set a session variable or cookie to keep the user logged in
                    request.session['admin_id'] = user.id
                    return redirect('admin_panel:admin_dashboard')  # Adjust this URL as needed
                else:
                    # Password is incorrect
                    form.add_error(None, "Invalid login credentials")
            except Admin.DoesNotExist:
                # Handle the case where the user does not exist
                form.add_error(None, "Invalid login credentials")
    else:
        form = AdminLoginForm()

    return render(request, 'admin_panel/login.html', {'form': form})


def admin_dashboard(request):
    
    pending_psm_requests = PSMRequest.objects.filter(status='Pending')
    rejected_psm_requests = PSMRequest.objects.filter(status='Rejected')
    approved_psm_requests = PSMRequest.objects.filter(status='Approved')

    pending_csr_requests = CSRRequest.objects.filter(status='Pending')
    rejected_csr_requests = CSRRequest.objects.filter(status='Rejected')
    approved_csr_requests = CSRRequest.objects.filter(status='Approved')

    context = {
        'pending_psm_requests': pending_psm_requests,
        'rejected_psm_requests': rejected_psm_requests,
        'approved_psm_requests': approved_psm_requests,
        'pending_csr_requests': pending_csr_requests,
        'rejected_csr_requests': rejected_csr_requests,
        'approved_csr_requests': approved_csr_requests,
    }

    return render(request, 'admin_panel/admin_dashboard.html', context)

def manage_surveyors(request):
    surveyors = Surveyor.objects.all()
    return render(request, 'admin_panel/manage_surveyors.html', {'surveyors': surveyors})


def edit_surveyor(request, surveyor_id):
    surveyor = get_object_or_404(Surveyor, pk=surveyor_id)
    
    if request.method == 'POST':
        form = SurveyorForm(request.POST, instance=surveyor)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:manage_surveyors')
    else:
        form = SurveyorForm(instance=surveyor)

    return render(request, 'admin_panel/edit_surveyor.html', {'form': form, 'surveyor': surveyor})

def create_surveyor(request):
    if request.method == 'POST':
        form = SurveyorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:manage_surveyors')
    else:
        form = SurveyorForm()

    return render(request, 'admin_panel/create_surveyor.html', {'form': form})

def manage_psms(request):
    psm_requests = PSMRequest.objects.filter()
    return render(request, 'admin_panel/manage_psms.html', {'psm_requests': psm_requests})

def manage_csrs(request):
    csr_requests = CSRRequest.objects.all()
    return render(request, 'admin_panel/manage_csrs.html', {'csr_requests': csr_requests})

def approve_psm_request(request):
    if request.method == 'POST':
        psm_request_id = request.POST.get('psm_request')
        psm_request = get_object_or_404(PSMRequest, id=psm_request_id)

        form = PSMRequestApprovalForm(request.POST, instance=psm_request)
        if form.is_valid():
            psm_request = form.save(commit=False)
            psm_request.status = 'Approved'
            psm_request.save()
            return redirect('admin_panel:admin_dashboard')
    else:
        form = PSMRequestApprovalForm()

    pending_psm_requests = PSMRequest.objects.filter(status='Pending')

    return render(request, 'admin_panel/approve_psm_request.html', {'form': form, 'pending_psm_requests': pending_psm_requests})

def approve_csr_request(request):
    if request.method == 'POST':
        csr_request_id = request.POST.get('csr_request')
        csr_request = get_object_or_404(CSRRequest, id=csr_request_id)

        form = CSRRequestApprovalForm(request.POST, instance=csr_request)
        if form.is_valid():
            csr_request = form.save(commit=False)
            csr_request.status = 'Approved'
            csr_request.save()
            return redirect('admin_panel:admin_dashboard')
    else:
        form = CSRRequestApprovalForm()

    pending_csr_requests = CSRRequest.objects.filter(status='Pending')

    return render(request, 'admin_panel/approve_csr_request.html', {'form': form, 'pending_csr_requests': pending_csr_requests})