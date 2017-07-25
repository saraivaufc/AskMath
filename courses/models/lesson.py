# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from django.db.models.signals import pre_save

from base.utils.models import AutoSlugField
from .learning_object import LearningObject

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
	
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['creation']
		verbose_name = _(u'Lesson')
		verbose_name_plural = _(u'Lessons')

class LearningObjectHistory(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"User"), blank=True)
	learning_object = models.ForeignKey('courses.LearningObject', verbose_name=_(u"Learning Object"), blank=True)
	active = models.BooleanField(verbose_name=_("Active"), default=True)
	
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return u"{0} >> {1}".format(self.user, self.learning_object)

	class Meta:
		ordering = ("-creation",)
		verbose_name = _(u'Learning Object History')
		verbose_name_plural = _(u'Learning Object History')

def clean_old_learning_object_history(sender, instance, ** kwargs):
	LearningObjectHistory.objects.filter(user=instance.user, learning_object__lesson=instance.learning_object.lesson).update(active=False)

pre_save.connect(clean_old_learning_object_history, sender=LearningObjectHistory)