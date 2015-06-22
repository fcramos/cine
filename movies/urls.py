# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('movies.views',
    url(r'^$', 'home', name='home'),
    url(r'^filme/(?P<slug>[\w-]+)/$', 'detail', name='detail'),
)