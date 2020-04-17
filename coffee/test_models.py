from django.test import TestCase
from .models import Coffee, Intensity, Comment

class TestItemModel(TestCase):
    def test_can_create_a_coffee_with_name_overview_and_price(self):
        coffee = Coffee(name='test',overview='test', price='1')
        coffee.save()
        self.assertEqual(coffee.name, 'test')
        self.assertEqual(coffee.overview, 'test')
        self.assertEqual(coffee.price, '1')

    def test_can_create_an_intensity_with_a_value(self):
        intensity = Intensity(intensity='1')
        intensity.save()
        self.assertEqual(intensity.intensity, '1')

    def test_can_create_a_comment_with_text(self):
        comment=Comment(text='test')
        self.assertEqual(comment.text, 'test')
      