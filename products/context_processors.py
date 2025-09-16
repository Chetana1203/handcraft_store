from .models import Order

def cart_items_count(request):
    if request.user.is_authenticated:
        # Get the user's active order (if exists)
        order = Order.objects.filter(customer=request.user, completed=False).first()
        if order:
            return {'cart_items_count': order.get_cart_items()}
    return {'cart_items_count': 0}