# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

BLOG_NAME = getattr(settings, 'BLOG_NAME', _('Blog'))
POST_IMAGE_DIR = getattr(settings, 'POST_IMAGE_DIR', 'uploads/post_photo/%Y/%m/%d')
