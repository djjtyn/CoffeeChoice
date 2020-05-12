from django.test import TestCase
from .forms import CommentForm

class TestCommentForm(TestCase):
    """test to check comment can be created"""
    def test_can_create_a_comment_with_just_text(self):
        form = CommentForm({'text': 'Create Tests'})
        self.assertTrue(form.is_valid())

    """test to check comment cant be created if there is no text"""
    def test_comment_cant_be_created_if_text_is_missing(self):
        form = CommentForm({'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [u'This field is required.'])