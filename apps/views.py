# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
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