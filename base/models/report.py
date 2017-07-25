# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

class Report(models.Model):
	name = models.CharField(verbose_name=_("Name"), max_length=100)
	email = models.EmailField(verbose_name=_("Email"))
	message = models.TextField(verbose_name=_("Message"))
	reply = models.TextField(verbose_name=_("Reply"), null=True, blank=True)

	solved_in = models.DateTimeField(verbose_name=_("Solved"), null=True, blank=True)
	solved_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Solved by"), related_name="report_solved_by", limit_choices_to={'is_staff': True}, null=True, blank=True)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Created by"), related_name="report_created_by", null=True, blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	ip_address = models.GenericIPAddressField(blank=True, null=True)

	def __unicode__(self):
		return '{0}-{1}'.format(self.name, self.message)

	class Meta:
		ordering = ['-last_modified']
		verbose_name = _('Report')
		verbose_name_plural = _('Reports')