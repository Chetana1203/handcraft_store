from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        products = Product.objects.filter(category_id=category_id)
        selected_category = Category.objects.get(id=category_id)
    else:
        products = Product.objects.all()
        selected_category = None

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'products/home.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)
