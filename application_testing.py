```python
import unittest
from django.test import Client
from django.urls import reverse
from product_catalog_app.models import Product

class TestViews(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('product_list')
        self.detail_url = reverse('product_detail', args=['1'])
        self.product1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            price=10.99,
            image='test_image1.jpg'
        )

    def test_product_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')

    def test_product_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')

    def test_product_create_POST(self):
        url = reverse('product_create')
        response = self.client.post(url, {
            'name': 'Test Product 2',
            'description': 'Test Description 2',
            'price': 20.99,
            'image': 'test_image2.jpg'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Product.objects.last().name, 'Test Product 2')

    def test_product_update_POST(self):
        url = reverse('product_update', args=['1'])
        response = self.client.post(url, {
            'name': 'Updated Product',
            'description': 'Updated Description',
            'price': 15.99,
            'image': 'updated_image.jpg'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Product.objects.get(id=1).name, 'Updated Product')

    def test_product_delete_GET(self):
        url = reverse('product_delete', args=['1'])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Product.objects.count(), 0)

if __name__ == "__main__":
    unittest.main()
```