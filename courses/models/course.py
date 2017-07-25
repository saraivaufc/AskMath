# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

import hashlib, collections

from base.utils.models import AutoSlugField

from courses import settings as local_settings
from courses.utils.lesson import LessonSorting

from .lesson import Lesson

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
	position = models.IntegerField(verbose_name=_("Position"), blank=True, unique=True)
	name = models.CharField(verbose_name=_(u"Name"), max_length=50, unique=True)
	description = models.TextField(verbose_name=_(u"Description"), max_length=200)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PUBLISHED)
	
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	@property
	def lessons(self):
		lessons = Lesson.objects.filter(courses=self, status=Lesson.PUBLISHED)
		lessons = LessonSorting(lessons).get_lessons()
		lessons = collections.OrderedDict(sorted(lessons.items()))
		return lessons

	def get_absolute_url(self):
		return reverse_lazy('courses:lesson_list', kwargs={'course_slug': self.slug})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['position', 'name']
		verbose_name = _(u'Course')
		verbose_name_plural = _(u'Courses')