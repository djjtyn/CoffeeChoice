from django.test import TestCase

class TestViews(TestCase):
    # View to make sure correct template is being rendered
    def test_get_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')