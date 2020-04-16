from django.conf.urls import url
from .views import filter_vertuo, filter_original

urlpatterns = [
    url(r'^vertuo$', filter_vertuo, name='filter_vertuo'),
    url(r'^original$', filter_original, name='filter_original')
]