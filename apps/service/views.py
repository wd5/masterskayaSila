# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, TemplateView
from apps.service.models import WorkCategory, Client, WorksMedia
from apps.clientsworks.models import ClientsWork
from apps.siteblocks.models import Blog

class ShowCategoriesView(ListView):
    model = WorkCategory
    template_name = 'service/categories_list.html'
    context_object_name = 'categories'
    queryset = model.objects.published()

show_categories = ShowCategoriesView.as_view()

class ShowCategoryView(DetailView):
    model = WorkCategory
    template_name = 'service/show_category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(ShowCategoryView, self).get_context_data(**kwargs)

        if self.object:
            if  self.object.id == 4:
                context['video_works_media'] = WorksMedia.objects.filter(work__workcategory__id=4).order_by('-work__date_create')[:self.object.works_count]

        text_parts = context['category'].description
        pos = text_parts.find('\n')
        context['category_descr_part1'] = text_parts[0:pos]
        context['category_descr_part2'] = text_parts[pos:]

        if context['category'].is_published == False:
            context['category'] = False

        try:
            blog_items = Blog.objects.published()
            blog_item = blog_items.order_by("?")[:1]
            context['blog_item'] = blog_item[0]
        except Blog.DoesNotExist:
            context['blog_item'] = False

        return context

show_work_category = ShowCategoryView.as_view()

class ShowClientsListView(ListView):
    model = Client
    template_name = 'service/clients_list.html'
    context_object_name = 'clients'
    queryset = model.objects.published()[:10]

show_clients_list = ShowClientsListView.as_view()


class ShowClientView(DetailView):
    model = Client
    template_name = 'service/show_client.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super(ShowClientView, self).get_context_data(**kwargs)

        if context['client'].is_published == False:
            context['client'] = False

        return context

show_client = ShowClientView.as_view()

class ShowMediaView(TemplateView):
    template_name = 'showmedia.html'

    def get_context_data(self, **kwargs):
        context = super(ShowMediaView, self).get_context_data(**kwargs)
        try:
            pk = int(self.kwargs.get('pk', None))
            type = self.kwargs.get('type', None)
        except:
            pk = False
            type = False

        if pk and type:
            if type == 'workmedia':
                code = WorksMedia.objects.get(id=pk)
            elif type == 'cabinetmedia':
                code = ClientsWork.objects.get(id=pk)
            else:
                code = False
        else:
            code = False

        context['code'] = code
        return context

show_media = ShowMediaView.as_view()