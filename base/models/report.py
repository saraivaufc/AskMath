# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

class Report(models.Model):
	page = models.URLField(verbose_name=_(u"Page"), blank=True)
	name = models.CharField(verbose_name=_(u"Name"), max_length=100, null=True, blank=True)
	email = models.EmailField(verbose_name=_(u"Email"), null=True, blank=True)
	message = models.TextField(verbose_name=_(u"Message"))

	
	solved_in = models.DateTimeField(verbose_name=_(u"Solved"), null=True, blank=True)
	solved_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Solved by"), related_name="report_solved_by", null=True, blank=True)
	
	creation = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="report_created_by", null=True, blank=True)
	last_modified = models.DateTimeField(auto_now=True)

	ip_address = models.GenericIPAddressField(blank=True, null=True)

	def __unicode__(self):
		return '{0}-{1}'.format(self.name, self.message)

	class Meta:
		ordering = ['-last_modified']
		verbose_name = _(u'Report')
		verbose_name_plural = _(u'Reports')