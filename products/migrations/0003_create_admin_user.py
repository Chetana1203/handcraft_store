from django.db import migrations
from django.contrib.auth.models import User
import os

def create_admin_user(apps, schema_editor):
    # Get credentials from environment or use defaults
    username = os.environ.get('ADMIN_USERNAME', 'admin')
    email = os.environ.get('ADMIN_EMAIL', 'admin@handcraftstore.com')
    password = os.environ.get('ADMIN_PASSWORD', 'admin123')
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)

def reverse_func(apps, schema_editor):
    # Optional: remove the admin user when migration is reversed
    username = os.environ.get('ADMIN_USERNAME', 'admin')
    User.objects.filter(username=username).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('products', '0002_alter_order_transaction_id'),
    ]
    
    operations = [
        migrations.RunPython(create_admin_user, reverse_func),
    ]