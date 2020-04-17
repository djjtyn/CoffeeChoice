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

    def test_get_comment_page(self):
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        blog = Post(title='Create a test')
        blog.save()
        page = self.client.get('/blog/post/{0}/comment/'.format(blog.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'add_comment_to_post.html')

