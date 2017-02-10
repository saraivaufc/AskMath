# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


COMMENT_MAX_LEN = 3000  # changing this needs migration

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('r', _('Removed')),
)

class Comment(models.Model):
	ancient = models.ForeignKey('self', verbose_name=_("Ancient"), null=True, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"))
	topic = models.ForeignKey('forum.Topic')

	text = models.TextField(_("Comment"), max_length=COMMENT_MAX_LEN)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)

	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	ip_address = models.GenericIPAddressField(blank=True, null=True)

	def __unicode__(self):
		return self.text

	class Meta:
		ordering = ['last_modified', ]
		verbose_name = _("Comment")
		verbose_name_plural = _("Comments")