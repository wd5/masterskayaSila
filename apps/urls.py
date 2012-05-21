# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

#from apps.app.urls import urlpatterns as app_url

from views import index,load_example
from apps.utils.utils import items_loader

urlpatterns = patterns('',
    url(r'^$',index, name='index'),
    (r'^load_items/$',items_loader),
    (r'^example/$',load_example),

)


