# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

PROFILE_IMAGE_DIR = getattr(settings, 'PROFILE_IMAGE_DIR', 'uploads/profile_image/%Y/%m/%d')

PERMISSIONS = getattr(settings, 'PERMISSIONS', {})
GROUP_PERMISSIONS = getattr(settings, 'GROUP_PERMISSIONS', {})
DEFAULT_GROUP = getattr(settings, 'DEFAULT_GROUP', None)
CONFIRM_EMAIL = getattr(settings, 'CONFIRM_EMAIL', False)