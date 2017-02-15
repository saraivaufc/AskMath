# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from .lesson import Lesson
from .choice import Choice
from .answer import Answer

class Question(models.Model):
	position = models.IntegerField(verbose_name=_(u"Position"), null=True, blank=True)
	introduction = models.ForeignKey("ask.Introduction", verbose_name=_(u"Introduction"), null=True, blank=True)
	text = models.TextField(verbose_name=_(u"Question text"))
	help = models.CharField(verbose_name=_(u"Help text"), max_length=255, null=True, blank=True)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="question_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	
	def get_choices(self):
		return Choice.objects.filter(question=self)

	def get_answers(self):
		return Answer.objects.filter(question=self)

	def __unicode__(self):
		return self.text[:50]

	class Meta:
		ordering = ['position', 'creation', 'last_modified']
		verbose_name = _(u'Question')
		verbose_name_plural = _(u'Questions')