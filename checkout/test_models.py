from django.test import TestCase
from .models import Order

class TestItemModel(TestCase):
    #test to check order can be created
    def test_can_create_order_with_name_phnumber_country_postcode_town_streetaddress_and_county(self):
        order = Order(full_name='test', phone_number='123', country='test',postcode='test',town_or_city='test',
        street_address1='test',street_address2='test',county='test')
        self.assertEqual(order.full_name, 'test')
        self.assertEqual(order.phone_number, '123')
        self.assertEqual(order.country, 'test')
        self.assertEqual(order.postcode, 'test')
        self.assertEqual(order.town_or_city, 'test')
        self.assertEqual(order.street_address1, 'test')
        self.assertEqual(order.street_address2, 'test')
        self.assertEqual(order.county, 'test')