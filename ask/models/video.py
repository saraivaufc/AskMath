# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from base.utils.models import AutoSlugField
from ..utils.colors import get_color

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('r', _('Removed')),
)

class Video(models.Model):
	position = models.IntegerField(verbose_name=_(u"Position"))
	title = models.CharField(verbose_name=_(u"Title"), max_length=255)
	slug = AutoSlugField(populate_from="title", db_index=False, blank=True, unique=True)
	description = models.TextField(verbose_name=_(u"Description"))
	url = models.URLField(verbose_name=_("URL"), max_length=500)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	color = models.CharField(max_length=20, default=get_color, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"User"), blank=True)
	
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['position']
		verbose_name = _(u'Video')
		verbose_name_plural = _(u'Videos')