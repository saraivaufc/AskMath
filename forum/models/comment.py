# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Comment(models.Model):
	DRAFT = 'd'
	PUBLISHED = 'p'
	REMOVED = 'r'
	STATUS_CHOICES = (
		(DRAFT, _('Draft')),
		(PUBLISHED, _('Published')),
		(REMOVED, _('Removed')),
	)
	ancient = models.ForeignKey('self', verbose_name=_("Ancient"), null=True, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"))
	topic = models.ForeignKey('forum.Topic')

	text = models.TextField(_("Text"))
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)

	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	ip_address = models.GenericIPAddressField(blank=True, null=True)

	def __unicode__(self):
		return self.text

	class Meta:
		ordering = ['creation',]
		verbose_name = _("Comment")
		verbose_name_plural = _("Comments")