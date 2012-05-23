# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

#from apps.app.urls import urlpatterns as app_url

from views import index,load_example
from apps.utils.utils import items_loader
from apps.service.views import show_work_category,show_client
from apps.siteblocks.views import show_blog_item

urlpatterns = patterns('',

    url(r'^$',index, name='index'),
    (r'^load_items/$',items_loader),

    (r'^example/$',load_example),

    (r'^services_and_works/$','apps.service.views.show_categories'),
    url(r'^services_and_works/(?P<slug>[^/]+)/$',show_work_category, name='show_work_category'),

    (r'^blog/$','apps.siteblocks.views.show_blog'),
    url(r'^blog/(?P<pk>[^/]+)/$',show_blog_item, name='show_blog_item'),

    (r'^clients/$','apps.service.views.show_clients_list'),
    url(r'^clients/(?P<slug>[^/]+)/$',show_client, name='show_client'),

)


