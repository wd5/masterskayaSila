# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from apps.siteblocks.models import Blog

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        #context['?????'] = ????????????
        return context

index = IndexView.as_view()

class LoaderExampleView(TemplateView):
    template_name = 'loader_example.html'

    def get_context_data(self, **kwargs):
        context = super(LoaderExampleView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.published()[:2]
        return context

load_example = LoaderExampleView.as_view()