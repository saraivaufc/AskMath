# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from base.utils.models import AutoSlugField
from ..utils.colors import get_color

class Video(models.Model):
	position = models.IntegerField(verbose_name=_(u"Position"), null=True, blank=True)
	title = models.CharField(verbose_name=_(u"Title"), max_length=255)
	slug = AutoSlugField(populate_from="title", db_index=False, blank=True, unique=True)
	description = models.TextField(verbose_name=_(u"Description"))
	url = models.URLField(verbose_name=_("URL"), max_length=500)
	color = models.CharField(max_length=20, default=get_color, blank=True)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="video_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['position', 'creation', 'last_modified']
		verbose_name = _(u'Video')
		verbose_name_plural = _(u'Videos')