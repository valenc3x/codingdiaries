from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout

urlpatterns = [
    # Base urls
    url(r'^$', 'codingdiaries.views.landing', name='landing'),
    url(r'^home$', 'codingdiaries.views.home', name='home'),
    url(r'^login$', 'codingdiaries.views.login_user', name='login'),
    url(r'^logout$', 'codingdiaries.views.logout_user', name='logout'),
    # Admin site
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
