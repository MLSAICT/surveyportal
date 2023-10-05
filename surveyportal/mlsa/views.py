from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Admin_users
from user.models import PSMRequest

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
    psm_table = PSMRequest.objects.all()
    for psm_request in psm_table:
        print(f"PSM Request ID: {psm_request.surveyor_name}")
    return render(request, 'mlsa/admindashboard.html', {
        'psm_table': psm_table
    })

def acceptpsmrequests(request):
    return render(request, 'mlsa/acceptpsmrequests.html')