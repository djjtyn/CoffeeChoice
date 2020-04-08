from django.conf.urls import url
from .views import all_coffee, coffee_review, add_comment_to_coffee

urlpatterns = [
    url(r'^all_coffee$', all_coffee, name='all_coffee'),
    url(r'^(?P<pk>\d+)/$', coffee_review, name='coffee_review'),
    url(r'^coffee/(?P<pk>\d+)/comment/$', add_comment_to_coffee, name='add_comment_to_coffee'),
]