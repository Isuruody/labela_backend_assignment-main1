from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Cart, Order, CartItem
from .serializers import ProductSerializer, CartSerializer, OrderSerializer, CartItemSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

class CreateProductView(generics.CreateAPIView):
    """
    View for creating a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser] 

class UpdateProductView(generics.UpdateAPIView):
    """
    View for updating an existing product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser] 

class DeleteProductView(generics.DestroyAPIView):
    """
    View for deleting an existing product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductListPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100  # Define the maximum page size

class ProductListView(generics.ListAPIView):
    """
    View for listing all available products with pagination.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price']
    
class ProductDetailView(generics.RetrieveAPIView):
    """
    View for viewing the details of a product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated] 

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated] 
    def put(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # For simplicity, let's assume that you're working with a single cart instance.
        # You can modify this logic if your application requires handling multiple carts.
        cart, created = Cart.objects.get_or_create(pk=1)  # Assuming the cart's primary key is 1

        # Check if the product is already in the cart
        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)

        cart_item_serializer = CartItemSerializer(cart_item)
        return Response(cart_item_serializer.data, status=status.HTTP_200_OK)


class RemoveFromCartView(APIView):
    """
    View for removing a product from the user's shopping cart.
    """
    permission_classes = [IsAuthenticated] 
    def put(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        # Assuming you're working with a single cart
        cart, created = Cart.objects.get_or_create(pk=1)  # Replace 1 with the actual cart's ID

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.delete()
            return Response({'detail': 'Product removed from the cart'}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({'detail': 'Product not found in the cart'}, status=status.HTTP_400_BAD_REQUEST)


class CartView(generics.RetrieveUpdateAPIView):
    """
    View for managing the user's shopping cart.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated] 

    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class OrderCreateView(CreateAPIView):
    """
    View for creating an order from the shopping cart.
    """
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] 

    def create(self, request, *args, **kwargs):
        # For simplicity, let's assume that We're working with a single cart instance.
        #  can modify this logic if our application requires handling multiple carts.
        cart, created = Cart.objects.get_or_create(pk=1)  # Assuming the cart's primary key is 1

        delivery_date = request.data.get('delivery_date')
        delivery_address = request.data.get('delivery_address')  # Extract delivery address from request data

        # Add more order-related fields as needed

        # Create the order without involving the user
        order = Order.objects.create(cart=cart, delivery_date=delivery_date, delivery_address=delivery_address)

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderDetailView(generics.RetrieveAPIView):
    """
    View for viewing the details of an order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] 
 
