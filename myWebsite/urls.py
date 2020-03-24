from django.conf.urls import url, include
from django.contrib import admin
from home import urls as home_urls
from accounts import urls as accounts_urls
from coffee import urls as coffee_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(home_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^coffee/', include(coffee_urls)),
]