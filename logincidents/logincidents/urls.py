from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from web.views import *
urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
