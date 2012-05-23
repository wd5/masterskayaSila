# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from apps.siteblocks.models import Blog
from apps.service.models import Work,WorkCategory

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        try:
            works = Work.objects.published()
        except Work.DoesNotExist:
            works = False

        if works:
            context['works'] = works.filter(is_on_main=True)[:4]
        else:
            context['works'] = False

        try:
            context['works_categories'] = WorkCategory.objects.published().order_by('id')[:5]
        except WorkCategory .DoesNotExist:
            context['works_categories'] = False

        return context

index = IndexView.as_view()

class LoaderExampleView(TemplateView):
    template_name = 'loader_example.html'

    def get_context_data(self, **kwargs):
        context = super(LoaderExampleView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.published()[:2]
        return context

load_example = LoaderExampleView.as_view()