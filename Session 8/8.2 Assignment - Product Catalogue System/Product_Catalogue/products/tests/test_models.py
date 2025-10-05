from django.test import TestCase
from products.models import Product

class TestModels(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name = 'Sample Product',
            description = 'A sample description',
            price = 200,
            category = 'electronics',
            stock_quantity= 10
        )
        
    def test_product_creation(self):
        self.assertIsInstance(self.product, Product)
        self.assertEqual(self.product.name, 'Sample Product')
        self.assertEqual(self.product.price, 200)
        self.assertEqual(self.product.stock_quantity, 10)
        self.assertEqual(self.product.category, 'electronics')
        
    def test_product_str(self):
        self.assertEqual(str(self.product), self.product.name)
        