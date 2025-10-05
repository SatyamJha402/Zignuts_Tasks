from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from products.models import Product
import json

class TestViews(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.lists_url = reverse('product-list')
        self.product = Product.objects.create(
            name = 'Sample Product',
            description = 'A sample description',
            price = 200,
            category = 'electronics',
            stock_quantity= 10
        )
        self.detail_url = reverse('product-detail', args=[self.product.id])
    
    def test_product_list(self):
        response = self.client.get(self.lists_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

    
    def test_product_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['id'], self.product.id)
        self.assertEqual(data['name'], self.product.name)
        
    def test_product_create(self):
        payload = {
            'name': 'New Product',
            'description': 'New description',
            'price': 1000,
            'stock_quantity': 5,
            'category': 'books'
        }
        response = self.client.post(self.lists_url, payload, format = 'json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 2)
    
    def test_product_update(self):
        payload = {'price':15}
        response = self.client.patch(self.detail_url, payload, format='json')
        self.assertEqual(response.status_code, 200)
        self.product.refresh_from_db()
        self.assertEqual(self.product.price, 15)
    
    def test_product_destroy(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0)