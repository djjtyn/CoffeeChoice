from django.test import TestCase
from .forms import OrderForm

class TestCommentForm(TestCase):
    def test_form_needs_all_fields_except_postcode_filled_to_be_valid(self):
        form = OrderForm({'full_name': '', 'phone_number': '', 'country': '', 'postcode': '', 'town_or_city':'', 
                          'street_address1': '', 'street_address2': '', 'county': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])
        self.assertEqual(form.errors['phone_number'], [u'This field is required.'])
        self.assertEqual(form.errors['country'], [u'This field is required.'])
        self.assertEqual(form.errors['town_or_city'], [u'This field is required.'])
        self.assertEqual(form.errors['street_address1'], [u'This field is required.'])
        self.assertEqual(form.errors['street_address2'], [u'This field is required.'])
        self.assertEqual(form.errors['county'], [u'This field is required.'])

    def test_form_doesnt_need_postcode_entered_to_be_valid(self):
        form = OrderForm({'full_name': 'test', 'phone_number': '1234', 'country': 'test', 'postcode': '', 
                          'town_or_city':'test', 'street_address1': 'test', 'street_address2': 'test', 'county': 'test'})
        self.assertTrue(form.is_valid())