# -*- coding: utf-8 -*-
from django.template.context import RequestContext
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render_to_response
from apps.clientsworks.models import Profile
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

class ShowCabinetView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated() and not request.user.is_staff:
            try:
                profile = Profile.objects.get(user=request.user.id)
            except:
                profile = False
            return render_to_response('clientsworks/show_cabinet.html', {'profile': profile},
                context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/')

#    def post(self, request, *args, **kwargs):
#        if request.user.is_authenticated() and not request.user.is_staff:
#            return HttpResponse()
#        else:
#            return HttpResponseRedirect('/')

show_cabinet = ShowCabinetView.as_view()