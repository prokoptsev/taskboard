# coding: utf-8
from __future__ import unicode_literals, absolute_import
from . import *

THIRD_PARTY_APPS += (
    'debug_toolbar',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + APPS

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

WSGI_APPLICATION = 'ws4redis.django_runserver.application'
