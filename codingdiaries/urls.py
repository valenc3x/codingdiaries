from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Base urls
    url(r'^$', 'codingdiaries.views.home', name='home'),
    # Admin site
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
