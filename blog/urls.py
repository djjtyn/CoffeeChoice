from django.conf.urls import url
from .views import all_posts, post_detail, create_or_edit_a_post

urlpatterns = [
    url(r'^$', all_posts, name='all_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_a_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_a_post, name='edit_post')
]