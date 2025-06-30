import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myjob.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('fauzimalikahmad', 'uzieahmad1002@gmail.com', 'f20021023')
    print("Superuser created")
else:
    print("Superuser already exists")
