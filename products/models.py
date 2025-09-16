from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # Add this import

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_id': self.id})

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"Order {self.id} - {self.customer.username}"
    
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total() for item in order_items])
        return total
    
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total
    
    # Add this method to get order status
    def get_status(self):
        return "Completed" if self.completed else "In Progress"
    
    # Add this class method to get user's order history
    @classmethod
    def get_user_order_history(cls, user):
        return cls.objects.filter(customer=user, completed=True).order_by('-created_at')

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    def get_total(self):
        return self.product.price * self.quantity