# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.inclusion_tag("items_loader/base_loader.html")
def block_items_loader(queryset,model_name,app_name,template_name,add_id,add_parameter):
    if add_parameter=='':
        add_parameter = False
    if add_id=='':
        add_id = False
    load_template = 'items_loader/%s_load_template.html' % template_name
    return {
        'items':queryset,
        'model_name':model_name,
        'app_name':app_name,
        'add_parameter':add_parameter,
        'add_id':add_id,
        'load_template':load_template,
        'template_name':template_name,
        'initial':True
    }