from django.test import TestCase
from products.models import Product

# Test case for the Product model
class TestModels(TestCase):
    # setup method to create a sample product before each test
    def setUp(self):
        self.product = Product.objects.create(
            name = 'Sample Product',
            description = 'A sample description',
            price = 200,
            category = 'electronics',
            stock_quantity= 10
        )
        
    # test to verify product creation
    def test_product_creation(self):
        # check if the product instance is created correctly
        self.assertIsInstance(self.product, Product)
        self.assertEqual(self.product.name, 'Sample Product') # verify name
        self.assertEqual(self.product.price, 200) # verify price
        self.assertEqual(self.product.stock_quantity, 10) # verify stock quantity
        self.assertEqual(self.product.category, 'electronics') # verify category
        
    # test to verify the string representation of the product
    def test_product_str(self):
        self.assertEqual(str(self.product), self.product.name)
        