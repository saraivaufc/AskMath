# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class EmailMarketing(models.Model):
	subject = models.CharField(verbose_name=_("Subject"), max_length=100)
	message = models.TextField(verbose_name=_("Message"))
	quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))

	receivers = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("Receivers"), related_name="email_marketing_receivers", blank=True)
	
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '{0}-{1}'.format(self.subject, self.message)

	class Meta:
		ordering = ['-creation']
		verbose_name = _('Email Marketing')
		verbose_name_plural = _('Email Marketings')