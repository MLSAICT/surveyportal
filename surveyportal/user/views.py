from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
##from surveyportal import settings
from user import db
import mysql.connector 
from .models import ReferenceLetterPSM, RequestLetterPSM
from .forms import ReferenceLetterPSMForm
from .forms import RequestLetterPSMForm
import os
from datetime import datetime
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
import shutil
from .models import PSMRequest
from .models import Islands
from .forms import PSMRequestForm
import pandas as pd
from.models import Islands
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .models import Surveyors
# Create your views here.

def index(request):
    return render(request, 'user/index.html')

def psm_request_detail(request, pk):
    psm_request = get_object_or_404(PSMRequest, pk=pk)
    return render(request, 'view_details.html', {'psm_request': psm_request})

def import_data_from_csv(file_path):
    data = pd.read_csv(file_path)  # Read the CSV file using pandas

    for index, row in data.iterrows():
        island_code = row['island_code']
        atoll = row['atoll']
        island_name = row['island_name']

    # Create or update the Islands object
        Islands.objects.update_or_create(
            island_code=island_code,
            defaults={'atoll': atoll, 'island_name': island_name}
        )

def login_user(request):
    if request.method == 'POST':
        license_number = request.POST.get('license_number')
        password = request.POST.get('password')

        if license_number and password:
            try:
                # Retrieve the user from the database using the provided license_number
                user = Surveyors.objects.get(license_number=license_number)
            except Surveyors.DoesNotExist:
                # Handle if the license_number is not found
                error = "Invalid license number"
                return render(request, 'user/login.html', {'error': error})

            # Verify the provided password with the one stored in the database
            if password == user.password:
                # Password matches, create a session for the user
                request.session['user_license_number'] = license_number
                return redirect('/userdashboard')
            else:
                # Handle invalid password here, such as displaying an error message
                error = "Invalid password"
                return render(request, 'user/login.html', {'error': error})
        else:
            # Handle missing credentials here, such as displaying an error message
            error = "Both license number and password are required"
            return render(request, 'user/login.html', {'error': error})

    return render(request, 'user/login.html')

    

def userdashboard(request):

    if not request.session.get('user_license_number'):
        return redirect('login')  # Redirect to login if not logged in

    user_license_number = request.session.get('user_license_number')
    user = get_object_or_404(Surveyors, license_number=user_license_number)

    if request.method == 'POST':
        psm_form = PSMRequestForm(request.POST)
        reference_form = ReferenceLetterPSMForm(request.POST, request.FILES, prefix='reference')
        request_form = RequestLetterPSMForm(request.POST, request.FILES, prefix='request')

        # Manually validate the forms
        psm_form_valid = psm_form.is_valid()
        reference_form_valid = reference_form.is_valid()
        request_form_valid = request_form.is_valid()

        if psm_form_valid and reference_form_valid and request_form_valid:

            psm_request = psm_form.save(commit=False)
            psm_request.surveyor_name = user.name
            psm_request.save()

            # Associate the ReferenceLetterPSM and RequestLetterPSM instances
            if reference_form.cleaned_data.get('document'):
                reference_letter_psm = ReferenceLetterPSM(document=reference_form.cleaned_data['document'])
                reference_letter_psm.save()
                psm_request.referenceletterpsm = reference_letter_psm

            if request_form.cleaned_data.get('document1'):
                request_letter_psm = RequestLetterPSM(document1=request_form.cleaned_data['document1'])
                request_letter_psm.save()
                psm_request.requestletterpsm = request_letter_psm

            psm_request.save()

            

            # Render success template or redirect to a success page
            request.session['user_license_number'] = user_license_number
            return render(request, 'user/userdashboard.html', {
                'psm_form': psm_form,
                'reference_form': reference_form,
                'request_form': request_form,
                'user': user
            })
        else:
            print("Form validation failed")

            # Print the form errors
            print("PSM Form errors:", psm_form.errors)
            print("Reference Form errors:", reference_form.errors)
            print("Request Form errors:", request_form.errors)

       
    else:
        psm_form = PSMRequestForm()
        reference_form = ReferenceLetterPSMForm(prefix='reference')
        request_form = RequestLetterPSMForm(prefix='request')
   

    island_display = PSMRequest.objects.filter(surveyor_name=user.name)
    print (island_display)
    

    return render(request, 'user/userdashboard.html', {
        'psm_form': psm_form,
        'reference_form': reference_form,
        'request_form': request_form,
        'island_display' : island_display,
        'user': user
        

    
    })

# def save_file(file, folder_name):
#     if file:
#         file_extension = os.path.splitext(file.name)[1]
#         timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
#         file_name = f"{timestamp}{file_extension}"
#         file_path = os.path.join(settings.MEDIA_ROOT, folder_name, file_name)
#         print(file_path)
#         file_path = file_path.replace("\\", "/")

#         with open(file_path, 'wb') as destination:
#             for chunk in file.chunks():
#                 destination.write(chunk)

#         return file_path

def beyrah(request):
    if 'user_license_number' in request.session:
        del request.session['user_license_number']
    return redirect('login')


# def save_form_with_folder(form, folder_name, field_name):
#     if form.is_valid():
#         file = form.cleaned_data[field_name]
#         file_extension = os.path.splitext(file.name)[1]
#         timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
#         file_name = f"{timestamp}{file_extension}"
#         file_path = os.path.join(settings.MEDIA_ROOT, folder_name, file_name)
#         print(file_path)
#         file_path = file_path.replace("\\", "/")
#         print(file_path)
#         with open(file_path, 'wb') as destination:
#             for chunk in file.chunks():
#                 destination.write(chunk)

#         setattr(form.instance, field_name, os.path.join(settings.MEDIA_URL, folder_name, file_name))
#         form.save()
        
#         print(file_path)
#         return file_path
#     return None



# def save_form_with_folder(form, folder_name, field_name, file_name_field):
#     if form.is_valid():
#         file = form.cleaned_data[field_name]
#         file_extension = os.path.splitext(file.name)[1]
#         timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
#         file_name = f"{timestamp}{file_extension}"
#         file_path = os.path.join(folder_name, file_name)

#         setattr(form.instance, file_name_field, file_path)  # Set the file path field of the instance
#         form.save()  # Save the form instance

#         return os.path.join(settings.MEDIA_ROOT, file_path)
#     return None


# def view_letter(request, file_path):
#     file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)
#     return FileResponse(open(file_full_path, 'rb'))

# def view_uploaded_document(request, model, pk):
#     if model == 'reference':
#         instance = get_object_or_404(ReferenceLetterPSM, pk=pk)
#         file_path = instance.document.name
#     elif model == 'request':
#         instance = get_object_or_404(RequestLetterPSM, pk=pk)
#         file_path = instance.document1.name
#     else:
#         return render(request, 'error.html')  # Handle invalid model parameter

#     file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)
#     destination_path = os.path.join(settings.BASE_DIR, 'permanent_files', file_path)
#     os.makedirs(os.path.dirname(destination_path), exist_ok=True)
#     shutil.copy(file_full_path, destination_path)

#     return FileResponse(open(destination_path, 'rb'), content_type='application/pdf')  # Assuming the files are PDFs

def view_uploaded_document(request, model, pk):
    if model == 'reference':
        instance = get_object_or_404(ReferenceLetterPSM, pk=pk)
    elif model == 'request':
        instance = get_object_or_404(RequestLetterPSM, pk=pk)
    else:
        # Handle invalid model parameter
        return render(request, 'error.html')

    file_path = instance.document.name
    file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)

    return FileResponse(open(file_full_path, 'rb'), content_type='application/pdf')  # Assuming the files are PDFs
def psmrequests(request):
    return render(request, 'user/psmrequests.html')

def usersettings(request):
    return render(request, 'user/settings.html')