#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def create_admin():
    import django
    from django.contrib.auth import get_user_model

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myjob.settings')
    django.setup()

    User = get_user_model()
    username = 'fauzimalik'
    password = 'fz0881'
    email = 'uziehamd1002@gmail.com'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f'Superuser "{username}" berhasil dibuat.')
    else:
        print(f'Superuser "{username}" sudah ada, tidak dibuat ulang.')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myjob.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Jalankan hanya saat migrate atau runserver dijalankan
    if len(sys.argv) > 1 and sys.argv[1] in ['runserver', 'migrate', 'runserver_plus']:
        create_admin()

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
