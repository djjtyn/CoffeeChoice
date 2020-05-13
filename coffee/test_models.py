from django.test import TestCase
from .models import Coffee, Intensity, Comment

class TestItemModel(TestCase):
    #test to check coffee can be created with string name and overview fields and integer price
    def test_can_create_a_coffee_with_name_overview_as_string_and_price_as_int(self):
        coffee = Coffee(name='test',overview='test', price=1)
        coffee.save()
        self.assertEqual(str(coffee.name), 'test')
        self.assertEqual(str(coffee.overview), 'test')
        self.assertEqual(int(coffee.price), 1)

    #test to check intensity can be created with interger intensity value
    def test_can_create_an_intensity_with_an_int_value(self):
        intensity = Intensity(intensity=1)
        intensity.save()
        self.assertEqual(int(intensity.intensity), 1)

    #test to check comment can be created with string text value
    def test_can_create_a_comment_with_string_text(self):
        comment=Comment(text='test')
        self.assertEqual(str(comment.text), 'test')
      