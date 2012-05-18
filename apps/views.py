# -*- coding: utf-8 -*-
from django.db.models.loading import get_model
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from apps.siteblocks.models import Blog
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

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

@csrf_exempt
def items_loader(request):
    if not request.is_ajax():
        return HttpResponseRedirect('/')
    else:
        if 'cnt' not in request.POST or 'init_cnt' not in request.POST or 'm_name' not in request.POST or 'a_name' not in request.POST:
            return HttpResponseBadRequest()

        count = request.POST['cnt']
        try:
            count = int(count)
        except ValueError:
            return HttpResponseBadRequest()

        initial_count = request.POST['init_cnt']
        try:
            initial_count = int(initial_count)
        except ValueError:
            return HttpResponseBadRequest()

        app_name = request.POST['a_name']
        model_name = request.POST['m_name']
        model = get_model(app_name, model_name)
        endrange = initial_count + count

        if model:
            try:
                queryset = model.objects.published()
                remaining_count = queryset.count() - endrange
                queryset = queryset[initial_count:endrange]
                if count<remaining_count:
                    remaining_count = False
            except model.DoesNotExist:
                return HttpResponseBadRequest()
        else:
            return HttpResponseBadRequest()

        response = HttpResponse()
        load_template = 'items_loader/%s_load_template.html' % model_name
        items_html = render_to_string(
            'items_loader/base_loader.html',
            {'items': queryset, 'load_template': load_template, 'endrange':endrange, 'remaining_count':remaining_count, }
        )
        response.content = items_html
        return response