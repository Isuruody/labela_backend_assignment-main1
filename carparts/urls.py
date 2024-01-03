from django.urls import path
from . import views

urlpatterns = [
    # Views for managing products (for companies)
    path('api/products/create/', views.CreateProductView.as_view(), name='create-product'),
    path('api/products/update/<int:pk>/', views.UpdateProductView.as_view(), name='update-product'),
    path('api/products/delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete-product'),

    # Views for listing and viewing product details
    path('api/products/', views.ProductListView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    # Views for managing the shopping cart
    path('api/cart/<int:pk>/', views.CartView.as_view(), name='cart'),
    path('api/cart/add/<int:product_id>/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('api/cart/remove/<int:product_id>/', views.RemoveFromCartView.as_view(), name='remove-from-cart'),

    # View for creating an order from the shopping cart
    path('api/order/create/', views.OrderCreateView.as_view(), name='create-order'),

    # View for viewing the details of an order
    path('api/order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]

