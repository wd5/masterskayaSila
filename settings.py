# -*- coding: utf-8 -*-
DATABASE_NAME = u'masterskayaSila'
PROJECT_NAME = u'masterskayaSila'
SITE_NAME = u'Мастерская сила'
DEFAULT_FROM_EMAIL = u'support@masterskayasila.octweb.ru'

from config.base import *

try:
    from config.development import *
except ImportError:
    from config.production import *

TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'apps.siteblocks',
    'apps.pages',
    'apps.service',
    'apps.clientsworks',

    'apps.utils.items_loader',

    'sorl.thumbnail',
    #'south',
    #'captcha',
)

MIDDLEWARE_CLASSES += (
    'apps.pages.middleware.PageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'apps.pages.context_processors.meta',
    'apps.siteblocks.context_processors.settings',
    'apps.utils.context_processors.authorization_form',
)