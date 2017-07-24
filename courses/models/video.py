# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from base.utils.models import AutoSlugField

class Video(models.Model):
	slug = AutoSlugField(populate_from="title", db_index=False, blank=True, unique=True)
	title = models.CharField(verbose_name=_(u"Title"), max_length=255)
	description = models.TextField(verbose_name=_(u"Description"))
	url = models.URLField(verbose_name=_("URL"))
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="video_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-creation',]
		verbose_name = _(u'Video')
		verbose_name_plural = _(u'Videos')