from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import ProductViewSet


class TestUrls(SimpleTestCase):
    
    def test_list_urls(self):
        url = reverse('product-list')
        print(resolve(url))
        self.assertEqual(resolve(url).url_name, 'product-list')
        
    def test_detail_urls(self):
        url = reverse('product-detail', args=[1])
        print(resolve(url))
        self.assertEqual(resolve(url).url_name, 'product-detail')