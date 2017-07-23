# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from base.utils.models import AutoSlugField

class Lesson(models.Model):
	DRAFT = 'd'
	PUBLISHED = 'p'
	REMOVED = 'r'
	STATUS_CHOICES = (
		(DRAFT, _('Draft')),
		(PUBLISHED, _('Published')),
		(REMOVED, _('Removed')),
	)
	slug = AutoSlugField(populate_from="name", db_index=False, blank=True, unique=True)
	courses = models.ManyToManyField("Course", verbose_name=_(u"Courses"), related_name='lesson_courses', blank=True)
	name = models.CharField(verbose_name=_(u"Name"), max_length=50)
	description = models.TextField(verbose_name=_(u"Description"), max_length=200)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	requirements = models.ManyToManyField("Lesson", verbose_name=_(u"Requirements"), related_name='lesson_requirements', blank=True)
	questions = models.ManyToManyField("Question", verbose_name=_(u"Questions"), related_name='lesson_question', blank=True)
	videos = models.ManyToManyField("Video", verbose_name=_(u"Videos"), related_name='lesson_video', blank=True)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="lesson_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		course = self.courses.filter(status='p').first()
		return reverse_lazy('courses:lesson_detail', kwargs={'course_slug': course.slug, 'slug': self.slug})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['creation']
		verbose_name = _(u'Lesson')
		verbose_name_plural = _(u'Lessons')