# -*- coding: utf-8 -*-
from apps.siteblocks.models import Settings
from settings import SITE_NAME

def settings(request):
    try:
        address = Settings.objects.get(name='address').value
    except Settings.DoesNotExist:
        address = False

    try:
        address_footer = Settings.objects.get(name='address_footer').value
    except Settings.DoesNotExist:
        address_footer = False

    try:
        phonenum = Settings.objects.get(name='phonenum').value
    except Settings.DoesNotExist:
        phonenum = False

    return {
        'address': address,
        'address_footer': address_footer,
        'phonenum': phonenum,
        'site_name': SITE_NAME,
        }