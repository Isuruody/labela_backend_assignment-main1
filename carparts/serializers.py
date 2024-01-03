from rest_framework import serializers
from .models import Product, Cart, CartItem, Order

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')

class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cart model.
    """
    class Meta:
        model = Cart
        fields = ('id', 'user', 'products')


class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the CartItem model.
    """

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    """
    class Meta:
        model = Order
        fields = ('id', 'user', 'cart', 'delivery_date', 'delivery_address')
