from django.test import TestCase

class TestViews(TestCase):
    #test to check cart page returns correct template
    def test_get_cart_page(self):
        page = self.client.get('/cart/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'cart.html')