# -*- coding: utf-8 -*-
from apps.service.models import Client
from django import template

register = template.Library()

@register.inclusion_tag("service/block_clients.html")
def block_clients():
    try:
        clients = Client.objects.published().filter(is_at_clientblock=True)
    except:
        clients = False
    return {'clients': clients}