from django.test import TestCase
from .models import Coffee

class TestViews(TestCase):
    def test_get_coffee_page(self):
        page = self.client.get('/coffee/all_coffee')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'all_coffee.html')

    def test_get_coffee_review_page(self):
        review = Coffee(price = 1.12)
        review.save()
        page = self.client.get('/coffee/{0}/'.format(review.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'coffeereview.html')