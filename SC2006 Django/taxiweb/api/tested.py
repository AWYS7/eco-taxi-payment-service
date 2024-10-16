# to test django set up

import os
import sys
import django

# Get the absolute path of the project directory (the directory containing 'taxiweb')
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project root to sys.path
sys.path.append(project_root)

# Set up the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taxiweb.settings')

# Initialize Django
django.setup()

from django.conf import settings

# Now you can safely access settings
print(f"Django is set up. DEBUG mode: {settings.DEBUG}")
