import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'handcraft_store.settings')
django.setup()

from django.contrib.auth.models import User

def main():
    # Get credentials from environment or use defaults
    username = os.environ.get('ADMIN_USERNAME', 'admin')
    email = os.environ.get('ADMIN_EMAIL', 'admin@handcraftstore.com')
    password = os.environ.get('ADMIN_PASSWORD', 'admin123')
    
    # Create or update admin user
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        user.set_password(password)
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print(f"✓ Updated admin user: {username}")
    else:
        User.objects.create_superuser(username, email, password)
        print(f"✓ Created admin user: {username}")
    
    print(f"🔑 Login with: {username} / {password}")
    print("⚠️  Change password after first login!")

if __name__ == "__main__":
    main()