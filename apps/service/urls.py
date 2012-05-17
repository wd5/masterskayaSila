# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

#from apps.app.urls import urlpatterns as app_url

from views import show_work_category,show_client

urlpatterns = patterns('',

    url(r'^works/(?P<slug>[^/]+)/$',show_work_category, name='show_work_category'),

    url(r'^clients/(?P<slug>[^/]+)/$',show_client, name='show_client'),

)

