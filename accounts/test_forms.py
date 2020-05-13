from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

class TestAuthForms(TestCase):

    # Test to make sure Login form works
    def test_login_form(self):
        form = UserLoginForm({
            'username':'dave',
            'password':'password12345'
        })
        self.assertTrue(form.is_valid())

    def test_login_form_fails_without_password(self):
        form = UserLoginForm({
            'username':'dave',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])

    # Test to make sure Registration form works and both passwords have to be the same
    def test_registration_form(self):
        form = UserRegistrationForm({
            'username':'dave',
            'email':'test@test.ie',
            'password1':'password',
            'password2':'password'
        })
        self.assertTrue(form.is_valid())

    # Test to make sure Registration form fails if password 1 and 2 are different
    def test_registration_form_wont_work_if_password1_and_2_are_different(self):
        form = UserRegistrationForm({
            'username':'dave',
            'email':'test@test.ie',
            'password1':'password1',
            'password2':'password2'
         })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords must match'])
        

    # Test to make sure Registration form fails if password 2 is missing
    def test_registration_form_fails_with_missing_password2(self):
        form = UserRegistrationForm({
            'username':'dave',
            'email':'test@test.ie',
            'password1':'password',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'This field is required.'])
  
