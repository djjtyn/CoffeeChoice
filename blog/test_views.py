from django.test import TestCase
from .models import Post

class TestViews(TestCase):
    def test_get_all_posts_page(self):
        page = self.client.get('/blog/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blogposts.html')

    def test_get_individual_posts_page(self):
        blog = Post(title='Create a test')
        blog.save()
        page = self.client.get('/blog/{0}/'.format(blog.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'postdetail.html')

