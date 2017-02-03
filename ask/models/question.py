# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from .choice import Choice

class Question(models.Model):
	position = models.IntegerField(verbose_name=_(u"Position"))
	text = models.TextField(verbose_name=_(u"Question text"))
	help = models.CharField(verbose_name=_(u"Help text"), max_length=255, null=True, blank=True)

	def get_choices(self):
		return Choice.objects.filter(question=self)

	def __unicode__(self):
		return self.text

	class Meta:
		verbose_name = _(u'Question')
		verbose_name_plural = _(u'Questions')