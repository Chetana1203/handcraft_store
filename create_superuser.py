import os
import django
from django.conf import settings

# Configure Django
if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'handcraft_store.settings')
    django.setup()

from django.contrib.auth.models import User

def main():
    username = os.environ.get('ADMIN_USERNAME', 'admin')
    email = os.environ.get('ADMIN_EMAIL', 'admin@handcraftstore.com')
    password = os.environ.get('ADMIN_PASSWORD', 'admin123')
    
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print(f"Password updated for user: {username}")
    else:
        User.objects.create_superuser(username, email, password)
        print(f"Superuser created: {username}")
    
    print("Superuser process completed successfully")

if __name__ == '__main__':
    main()