# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

import hashlib

from courses import settings as local_settings

from base.utils.models import AutoSlugField

class Course(models.Model):
	DRAFT = 'd'
	PUBLISHED = 'p'
	REMOVED = 'r'
	STATUS_CHOICES = (
		(DRAFT, _('Draft')),
		(PUBLISHED, _('Published')),
		(REMOVED, _('Removed')),
	)
	slug = AutoSlugField(populate_from="name", db_index=False, blank=True, unique=True)
	position = models.IntegerField(verbose_name=_("Position"))
	name = models.CharField(verbose_name=_(u"Name"), max_length=50)
	description = models.TextField(verbose_name=_(u"Description"), max_length=200)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="course_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse_lazy('courses:lesson_list', kwargs={'course_slug': self.slug})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['position']
		verbose_name = _(u'Course')
		verbose_name_plural = _(u'Courses')