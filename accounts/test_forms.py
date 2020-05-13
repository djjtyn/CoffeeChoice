from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

class TestAuthForms(TestCase):

    def test_login_form(self):
        form = UserLoginForm({
            'username':'dave',
            'password':'password12345'
        })
        self.assertTrue(form.is_valid())

    def test_registration_form(self):
        form = UserRegistrationForm({
            'username':'dave',
            'email':'test@test.ie',
            'password1':'password',
            'password2':'password'
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_wont_work_if_password1_and_2_are_different(self):
        form = UserRegistrationForm({
            'username':'dave',
            'email':'test@test.ie',
            'password1':'password1',
            'password2':'password2'
         })
        self.assertFalse(form.is_valid())

    def test_registration_form_will_work_if_password1_and_2_are_identical(self):
        form = UserRegistrationForm({
            'username':'dave',
            'email':'test@test.ie',
            'password1':'password',
            'password2':'password',
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_password2(self):
        form = UserRegistrationForm({
            'username':'dave',
            'email':'test@test.ie',
            'password1':'password',
        })
        self.assertFalse(form.is_valid())
  
