# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

#from apps.app.urls import urlpatterns as app_url

from views import index,load_example
from apps.utils.utils import items_loader
from apps.service.views import show_work_category,show_client

urlpatterns = patterns('',
    url(r'^$',index, name='index'),
    (r'^load_items/$',items_loader),

    (r'^example/$',load_example),

    url(r'^works/(?P<slug>[^/]+)/$',show_work_category, name='show_work_category'),
    url(r'^clients/(?P<slug>[^/]+)/$',show_client, name='show_client'),


)


