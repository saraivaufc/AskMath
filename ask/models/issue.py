# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from base.utils.models import AutoSlugField

from ..utils.colors import get_color

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('r', _('Removed')),
)

class Issue(models.Model):
	name = models.CharField(verbose_name=_(u"Name"), max_length=255)
	slug = AutoSlugField(populate_from="name", db_index=False, blank=True, unique=True)
	icon = models.ImageField(verbose_name=_(u"Icon"), upload_to=settings.ISSUE_PHOTO_DIR, null=True, blank=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	color = models.CharField(max_length=20, default=get_color, blank=True)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="issue_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True) 


	def get_absolute_url(self):
		return reverse_lazy('ask:lesson_list', kwargs={'issue_slug': self.slug})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _(u'Issue')
		verbose_name_plural = _(u'Issues')