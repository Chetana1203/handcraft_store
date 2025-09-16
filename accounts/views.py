from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from products.models import Order  # Add this import

# Add this helper function (same as in products/views.py)
def get_cart_count(user):
    """Helper function to get cart item count for a user"""
    if user.is_authenticated:
        order = Order.objects.filter(customer=user, completed=False).first()
        if order:
            return order.get_cart_items()
    return 0

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
        'cart_count': get_cart_count(request.user)  # Add this
    }
    return render(request, 'accounts/register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    context = {
        'cart_count': get_cart_count(request.user)  # Add this
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')