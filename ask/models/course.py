# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

import hashlib

from ask import settings as local_settings

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
	name = models.CharField(verbose_name=_(u"Name"), max_length=255)
	icon = models.ImageField(verbose_name=_(u"Icon"), upload_to=local_settings.COURSE_ICON_DIR)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="course_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True) 

	def save(self, *args, **kwargs):
		if not self.id and self.icon:
			hash = hashlib.md5(self.icon.read()).hexdigest()
			if self.icon.name.find(hash) == -1:
				self.icon.name = "".join((hash, ".", self.icon.name.split(".")[-1]))
		super(Course, self).save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse_lazy('ask:lesson_list', kwargs={'course_slug': self.slug})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _(u'Course')
		verbose_name_plural = _(u'Courses')