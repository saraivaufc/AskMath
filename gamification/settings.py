# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

LEVEL_IMAGE_DIR = getattr(settings, 'LEVEL_IMAGE_DIR', 'uploads/level_image/%Y/%m/%d')
