from django.conf.urls import url
from .views import all_coffee

urlpatterns = [
    url(r'^all_coffee$', all_coffee, name='all_coffee'),
]