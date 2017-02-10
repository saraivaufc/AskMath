# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

class Choice(models.Model):
	question = models.ForeignKey('Question', verbose_name=_(u'Question'))
	text = models.CharField(verbose_name=_(u"Choice text"), max_length=255)
	is_correct = models.BooleanField(verbose_name=_(u"Is correct"), default=False)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="choice_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.text

	class Meta:
		ordering = ['-last_modified']
		verbose_name = _(u'Choice')
		verbose_name_plural = _(u'Choices')