# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

COURSE_ICON_DIR = getattr(settings, 'COURSE_ICON_DIR', 'uploads/course_icon/%Y/%m/%d')
