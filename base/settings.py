# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

#definitions
SITE_NAME = getattr(settings, 'SITE_NAME', '')
SITE_URL = getattr(settings, 'SITE_URL', '')
SITE_AUTHOR = getattr(settings, 'SITE_AUTHOR', '')
SITE_DESCRIPTION = getattr(settings, 'SITE_DESCRIPTION', '')
SITE_HOME = getattr(settings, 'SITE_HOME', '/')

#media
SOCIAL_NETWORK_ICON_DIR = getattr(settings, 'SOCIAL_NETWORK_ICON_DIR', 'uploads/social_network_icon/%Y/%m/%d')