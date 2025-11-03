# from django.shortcuts import render
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import viewsets

# Using ModelViewSet to provide CRUD operations for Product model
class ProductViewSet(viewsets.ModelViewSet):
    # Define the queryset and serializer class
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    