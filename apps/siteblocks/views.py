# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from apps.service.models import WorkCategory
from apps.siteblocks.models import Blog

class ShowBlogView(ListView):
    model = Blog
    template_name = 'siteblocks/blog_list.html'
    context_object_name = 'blog'
    queryset = model.objects.published()[:4]

show_blog = ShowBlogView.as_view()

class ShowBlogItemView(DetailView):
    model = Blog
    template_name = 'siteblocks/show_blog_item.html'
    context_object_name = 'blog_item'

    def get_context_data(self, **kwargs):
        context = super(ShowBlogItemView, self).get_context_data(**kwargs)

        if context['blog_item'].is_published == False:
            context['blog_item'] = False

        return context

show_blog_item = ShowBlogItemView.as_view()