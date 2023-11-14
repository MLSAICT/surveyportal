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


import csv
from admin_panel.models import Island 
import pandas as pd


csv_file = 'Island.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Assuming you have a model named Island with fields 'code', 'atoll', and 'name'
# You can create records from the DataFrame like this:
for _, row in df.iterrows():
    code = row['FCODE']
    atoll = row['atoll']
    name = row['islandName']
    
    # Create an Island record with the extracted data
    Island.objects.create(code=code, atoll=atoll, name=name)