# survey_portal/surveyor/views.py
from django.shortcuts import render, redirect
from .models import Surveyor, PSMRequest, CSRRequest
from .forms import PSMRequestForm, CSRRequestForm, SurveyorLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
import logging
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

def custom_login(request):
    if request.method == 'POST':
        form = SurveyorLoginForm(request.POST)
        if form.is_valid():
            license_number = form.cleaned_data['license_number']
            password = form.cleaned_data['password']

            try:
                surveyor = Surveyor.objects.get(license_number=license_number)
            except Surveyor.DoesNotExist:
                logger.error(f"Surveyor not found with license number: {license_number}")
                return render(request, 'surveyor/login.html', {'error': 'Invalid login credentials'})

            if surveyor.check_password(password):
                request.session['surveyor_id'] = surveyor.id
                return redirect('surveyor:surveyor_dashboard')
            else:
                logger.error(f"Invalid password for license number: {license_number}")
                return render(request, 'surveyor/login.html', {'error': 'Invalid password'})
        else:
            logger.error("Form validation failed")
            return render(request, 'surveyor/login.html', {'form': form})
    else:
        form = SurveyorLoginForm()

    return render(request, 'surveyor/login.html', {'form': form})


def surveyor_dashboard(request):
    surveyor_id = request.session.get('surveyor_id')
    if surveyor_id:
        try:
            surveyor = Surveyor.objects.get(id=surveyor_id)
            psm_requests = PSMRequest.objects.filter(surveyor=surveyor)
            csr_requests = CSRRequest.objects.filter(surveyor=surveyor)
            return render(request, 'surveyor/dashboard.html', {'surveyor': surveyor, 'psm_requests': psm_requests, 'csr_requests': csr_requests})
        except Surveyor.DoesNotExist:
            logger.error(f"Surveyor not found for user ID: {surveyor_id}")
    return render(request, 'surveyor/dashboard.html', {'error': 'Surveyor not found'})

def submit_psm_request(request):
    if request.method == 'POST':
        form = PSMRequestForm(request.POST, request.FILES)
        if form.is_valid():
            surveyor_id = request.session.get('surveyor_id')
            if surveyor_id:
                surveyor = get_object_or_404(Surveyor, id=surveyor_id)
                form.instance.surveyor = surveyor
                form.save()
                return redirect('surveyor:surveyor_dashboard')
    else:
        form = PSMRequestForm()
    return render(request, 'surveyor/submit_psm_request.html', {'form': form})

def submit_csr_request(request):
    if request.method == 'POST':
        form = CSRRequestForm(request.POST, request.FILES)
        if form.is_valid():
            surveyor_id = request.session.get('surveyor_id')
            if surveyor_id:
                surveyor = get_object_or_404(Surveyor, id=surveyor_id)
                form.instance.surveyor = surveyor
                form.save()
                return redirect('surveyor:surveyor_dashboard')
    else:
        form = CSRRequestForm()
    return render(request, 'surveyor/submit_csr_request.html', {'form': form})