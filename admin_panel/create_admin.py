import os
import sys
from django.conf import settings

# Find the project's base directory (where manage.py is located)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Append the project's base directory to the system path
sys.path.append(base_dir)

# Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'survey_portal.settings'

# Initialize Django
import django
django.setup()

# Now you can import your models
from admin_panel.models import Admin  # Replace 'admin_panel' with your app name

# Create an admin user
admin = Admin.objects.create_user(username='admin', password='adminpassword')
admin.save()

print("Admin user created successfully.")
