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

def category_pic(id,size):
    if id==4:
        path = '/media/img/video_%s.png' % size
    elif id==5:
        path = '/media/img/design_%s.png' % size
    elif id==2:
        path = '/media/img/foto_%s.png' % size
    elif id==1:
        path = '/media/img/out_adv_%s.png' % size
    elif id==3:
        path = '/media/img/smi_%s.png' % size
    elif id==6:
        path = '/media/img/prod_%s.png' % size
    else:
        path = ''
    return path

register.simple_tag(category_pic)

def category_href(id):
    if id==4:
        href = 'video_examples'
    elif id==5:
        href = 'design_examples'
    elif id==2:
        href = 'foto_examples'
    elif id==1:
        href = 'out_adv_examples'
    elif id==3:
        href = 'smi_examples'
    elif id==6:
        href = 'pred_examples'
    else:
        href = ''
    return href

register.simple_tag(category_href)