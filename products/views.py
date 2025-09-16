from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def get_cart_count(user):
    """Helper function to get cart item count for a user"""
    if user.is_authenticated:
        order = Order.objects.filter(customer=user, completed=False).first()
        if order:
            return order.get_cart_items()
    return 0

@login_required
def checkout(request):
    order = Order.objects.filter(customer=request.user, completed=False).first()
    if order and order.orderitem_set.exists():
        order.completed = True
        order.save()
        messages.success(request, "Order placed successfully!")
        context = {
            'order': order,
            'cart_count': get_cart_count(request.user)
        }
        return render(request, 'products/checkout.html', context)
    messages.warning(request, "Your cart is empty")
    return redirect('cart')

# Add this new view for order history
@login_required
def order_history(request):
    """View to display user's order history"""
    orders = Order.get_user_order_history(request.user)
    
    context = {
        'orders': orders,
        'cart_count': get_cart_count(request.user)
    }
    return render(request, 'products/order_history.html', context)

# Add this view for order detail
@login_required
def order_detail(request, order_id):
    """View to display details of a specific order"""
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    
    context = {
        'order': order,
        'cart_count': get_cart_count(request.user)
    }
    return render(request, 'products/order_detail.html', context)

# Keep your existing views (home, product_detail, cart, etc.)
def home(request):
    # Get all categories for the filter menu
    categories = Category.objects.all()
    
    # Get the selected category from the request
    category_id = request.GET.get('category')
    
    if category_id:
        # Filter products by category
        products = Product.objects.filter(category_id=category_id)
        selected_category = Category.objects.get(id=category_id)
    else:
        # Show all products
        products = Product.objects.all()
        selected_category = None
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'cart_count': get_cart_count(request.user)
    }
    return render(request, 'products/home.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
        'cart_count': get_cart_count(request.user)  # Add this
    }
    return render(request, 'products/product_detail.html', context)

@login_required
def cart(request):
    order, created = Order.objects.get_or_create(
        customer=request.user, 
        completed=False
    )
    items = order.orderitem_set.all()
    
    context = {
        'order': order,
        'items': items,
        'cart_count': get_cart_count(request.user)  # Add this
    }
    return render(request, 'products/cart.html', context)

@login_required
def checkout(request):
    order = Order.objects.filter(customer=request.user, completed=False).first()
    if order and order.orderitem_set.exists():
        order.completed = True
        order.save()
        messages.success(request, "Order placed successfully!")
        context = {
            'order': order,
            'cart_count': get_cart_count(request.user)  # Add this
        }
        return render(request, 'products/checkout.html', context)
    messages.warning(request, "Your cart is empty")
    return redirect('cart')

# Keep your other view functions the same (add_to_cart, update_cart, remove_from_cart)
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(
        customer=request.user, 
        completed=False
    )
    order_item, created = OrderItem.objects.get_or_create(
        product=product, 
        order=order
    )
    
    if not created:
        order_item.quantity += 1
        order_item.save()
        messages.success(request, f"Added another {product.name} to cart")
    else:
        messages.success(request, f"Added {product.name} to cart")
    
    return redirect('product_detail', product_id=product_id)

@login_required
def update_cart(request, item_id, action):
    order_item = get_object_or_404(OrderItem, id=item_id)
    
    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1
    
    order_item.save()
    
    if order_item.quantity <= 0:
        order_item.delete()
        messages.info(request, "Item removed from cart")
    
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    order_item = get_object_or_404(OrderItem, id=item_id)
    product_name = order_item.product.name
    order_item.delete()
    messages.info(request, f"{product_name} removed from cart")
    return redirect('cart')