from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    """
    Represents a car part in the system.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed (e.g., part number, manufacturer, etc.)

    def __str__(self):
        return self.name

    @staticmethod
    def can_add_product(user):
        return user.is_staff  # Only allow admin users to add products

class Cart(models.Model):
    """
    Represents a user's shopping cart.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a user field
    products = models.ManyToManyField(Product, through='CartItem')
    
    def __str__(self):
        return f'Cart'

class CartItem(models.Model):
    """
    Represents an item in the shopping cart.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    """
    Represents an order placed by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a user field
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()
    delivery_address = models.CharField(max_length=255)
    # Add more fields as needed (e.g. payment status, etc.)

    def __str__(self):
        return f'Order'

    @staticmethod
    def can_place_order(user):
        return not user.is_anonymous  # Allow authenticated users to place orders
