from rest_framework import serializers
from products.models import Product

# The serializer translates the model instances into JSON format and vice versa
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'category']
        read_only_field = ['id'] # ID should not be modified directly