# -*- coding: utf-8 -*-
from apps.siteblocks.models import Settings
from django import template

register = template.Library()

@register.inclusion_tag("siteblocks/block_setting.html")
def block_static(name):
    try:
        setting = Settings.objects.get(name = name)
    except Settings.DoesNotExist:
        setting = False
    return {'block': block,}

@register.inclusion_tag("siteblocks/block_adv_maintenance.html")
def block_adv_maintenance(type):
    try:
        adv_m_texts = Settings.objects.filter(name__contains='adv_maintenance')
    except Settings.DoesNotExist:
        adv_m_texts = False

    if adv_m_texts:
        adv_first_text = adv_m_texts[0]
        adv_second_text = adv_m_texts[1]
    else:
        adv_first_text = False
        adv_second_text = False

    return {'adv_first_text': adv_first_text, 'adv_second_text': adv_second_text, 'type':type, }

