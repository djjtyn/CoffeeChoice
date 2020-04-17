from django.test import TestCase

class TestViews(TestCase):
    def test_get_cart_page(self):
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')