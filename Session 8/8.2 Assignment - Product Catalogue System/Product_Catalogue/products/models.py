from django.db import models
from django.core.validators import MinValueValidator

CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('clothing', 'Clothing'),
    ('home_appliances', 'Home Appliances'),
    ('books', 'Books'),
]

#  Fields: name, description, price, stock_quantity, category 
class Product(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, validators=[MinValueValidator(0.01)])
    stock_quantity = models.PositiveIntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    
    def __str__(self):
        return self.name