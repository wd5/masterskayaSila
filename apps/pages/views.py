# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.generic.simple import direct_to_template
from apps.pages.models import Page
from apps.siteblocks.models import Settings
import settings

def index(request):
    try:
        page = Page.objects.get(url = 'index')
    except Page.DoesNotExist:
        page = False
    return direct_to_template(request, 'pages/index.html', locals())

@csrf_protect
def page(request, url):
    if not url.endswith('/'):
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    page = get_object_or_404(Page, url__exact=url)
    #return direct_to_template(request, 'pages/default.html', locals())
    return render_to_response('pages/default.html', { 'page':page }, context_instance=RequestContext(request))

@csrf_exempt
def static_page(request, template):
    #return direct_to_template(request, template, locals())
    return render_to_response(template, locals(), context_instance=RequestContext(request))