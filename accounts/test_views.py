from django.test import TestCase

class TestViews(TestCase):
    """test to check login page is using correct template"""
    def test_get_login_page(self):
        page = self.client.get('/accounts/login/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')

    """test to check registration page is using correct template"""
    def test_get_registration_page(self):
        page = self.client.get('/accounts/register/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration.html')