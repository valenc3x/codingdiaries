from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Base urls
    url(r'^$', 'codingdiaries.views.landing', name='landing'),
    url(r'^home$', 'codingdiaries.views.home', name='home'),
    url(r'^login$', 'codingdiaries.views.login' , name='login'),
    # Admin site
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
