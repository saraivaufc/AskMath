# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

class Report(models.Model):
	page = models.URLField(verbose_name=_(u"Page"), blank=True)
	report_text = models.TextField(verbose_name=_(u"Report text"))
	
	solved = models.DateTimeField(verbose_name=_(u"Solved"), null=True, blank=True)
	solved_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Solved by"), related_name="report_solved_by", null=True, blank=True)
	
	creation = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="report_created_by", blank=True)
	last_modified = models.DateTimeField(auto_now=True)

	ip_address = models.GenericIPAddressField(blank=True, null=True)

	def __unicode__(self):
		return self.report_text

	class Meta:
		ordering = ['-last_modified']
		verbose_name = _(u'Report')
		verbose_name_plural = _(u'Reports')