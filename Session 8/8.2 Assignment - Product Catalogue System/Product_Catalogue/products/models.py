from django.db import models
from django.core.validators import MinValueValidator

# Predefined category choices
CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('clothing', 'Clothing'),
    ('home_appliances', 'Home Appliances'),
    ('books', 'Books'),
]

#  Fields: name, description, price, stock_quantity, category 
class Product(models.Model):
    name = models.CharField(max_length = 50, unique=True) # Product name should be unique
    description = models.TextField(max_length=500, blank=True) # description can be optional
    price = models.DecimalField(max_digits = 10, decimal_places = 2, validators=[MinValueValidator(0.01)]) # price should be positive and can be in decimal too
    stock_quantity = models.PositiveIntegerField() # stock quantity should be positive
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20) # category with predefined choices
    
    # represent the object as a string while displaying
    def __str__(self):
        return self.name