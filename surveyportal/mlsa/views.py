from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Admin_users
from user.models import PSMRequest
from .forms import CommentForm
from .models import UpdateLog
from django.utils import timezone

# Create your views here.
def login_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        if name and password:
            try:
                
                user = Admin_users.objects.get(name=name)
            except Admin_users.DoesNotExist:
                
                error = "Admin user does not exist  "
                print("User not found")
                return render(request, 'mlsa/alogin.html', {'error': error})

            # Verify the provided password with the one stored in the database
            if password == user.password:
                # Password matches, create a session for the user
                request.session['admin_name'] = name
                print("falied to send not found")
                return redirect('/admindashboard')
            else:
                # Handle invalid password here, such as displaying an error message
                error = "Invalid password"
                print("Password bad")
                return render(request, 'mlsa/alogin.html', {'error': error})
        else:
            # Handle missing credentials here, such as displaying an error message
            error = "Both username and password are required"
            print("BOTH WRONG")
            return render(request, 'mlsa/alogin.html', {'error': error})
        

    

    return render(request, 'mlsa/alogin.html')

def admindashboard(request):
    
    return render(request, 'mlsa/admindashboard.html')

def acceptpsmrequests(request, ):
    psm_table = PSMRequest.objects.all()
    
    status_updater = True
    if request.method == 'POST':
        psm_request_id = request.POST['psm_request_id']
        psm_request = PSMRequest.objects.get(id=psm_request_id)

        if 'approve' in request.POST:
            # Handle approval logic here
            psm_request.status = True  # Set status to approved
            update_log_entry = UpdateLog(
                psm_request=psm_request,
                date=timezone.now(),  # Add the current date
                staff=...,  # Add the staff member who approved
                description='Approved',
                comment=psm_request.comment,  # Add any comments
            )
            update_log_entry.save()

        elif 'reject' in request.POST:
            # Handle rejection logic here
            psm_request.status = False  # Set status to rejected
            update_log_entry = UpdateLog(
                psm_request=psm_request,
                date=timezone.now(),  # Add the current date
                staff=...,  # Add the staff member who rejected
                description='Rejected',
                comment=psm_request.comment,  # Add any comments
            )
            update_log_entry.save()


        psm_request.save()  # Update the existing PSMRequest

        # Handle the comment form separately
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the comment file to the corresponding PSMRequest
            psm_request.comment = form.cleaned_data['comment']
            psm_request.save()

        # You might want to add a success message or redirect to another page

    else:
        form = CommentForm()

    accepted_requests = psm_table.filter(status=True)
    rejected_requests = psm_table.filter(status=False)

    print ("RECENT:", psm_table)
    print ("ACCEPTED:", accepted_requests)
    print ("REJECTED:", rejected_requests)


    return render(request, 'mlsa/acceptpsmrequests.html', {
        'psm_table': psm_table,
        'form': form,
        'accepted_requests': accepted_requests,
        'rejected_requests': rejected_requests,
    })

