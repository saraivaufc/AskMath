# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

class LearningObject(models.Model):
	lesson = models.ForeignKey("courses.Lesson", verbose_name=_("Lesson"), related_name="slide_lesson")
	position = models.IntegerField(verbose_name=_("Position"))
	question = models.ForeignKey("courses.Question", verbose_name=_("Question"), related_name="slide_question", blank=True, null=True)

	creation = models.DateTimeField(auto_now_add=True)

	@property
	def next(self):
		return LearningObject.objects.filter(lesson=self.lesson, position__gte=self.position).exclude(pk=self.pk).order_by('position').first()

	@property
	def previous(self):
		return LearningObject.objects.filter(lesson=self.lesson, position__lte=self.position).exclude(pk=self.pk).order_by('-position').first()

	def __unicode__(self):
		return str(self.position)

	class Meta:
		ordering = ['position']
		verbose_name = _(u'Learning Object')
		verbose_name_plural = _(u'Learning Objects')
		unique_together = (('lesson', 'position'),)