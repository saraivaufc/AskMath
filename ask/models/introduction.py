# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from base.utils.models import AutoSlugField

class Introduction(models.Model):
	text = models.TextField(verbose_name=_(u"Introduction text"))

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="introduction_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return self.text[:50]

	class Meta:
		ordering = ['creation']
		verbose_name = _(u'Introduction')
		verbose_name_plural = _(u'Introductions')