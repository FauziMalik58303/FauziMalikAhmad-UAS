import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myjob.settings')
django.setup()

from django.contrib.auth.models import User, Group

if not User.objects.filter(username='fauzimalikahmad').exists():
    user = User.objects.create_superuser('fauzimalikahmad', 'uzieahmad1002@gmail.com', 'f20021023')
    print("Superuser created")
else:
    user = User.objects.get(username='fauzimalikahmad')
    print("Superuser already exists")

# Pastikan grup 'Operator' ada
operator_group, created = Group.objects.get_or_create(name='Operator')

# Masukkan superuser ke grup Operator (jika belum masuk)
if not user.groups.filter(name='Operator').exists():
    user.groups.add(operator_group)
    user.save()
    print("User added to Operator group")
else:
    print("User already in Operator group")
