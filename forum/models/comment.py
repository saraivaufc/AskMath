# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


COMMENT_MAX_LEN = 3000  # changing this needs migration

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('w', _('Withdrawn')),
)

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"))
	topic = models.ForeignKey('forum.Topic')

	text = models.TextField(_("Comment text"), max_length=COMMENT_MAX_LEN)
	date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	
	is_removed = models.BooleanField(default=False)
	ip_address = models.GenericIPAddressField(blank=True, null=True)

	def __unicode__(self):
		return self.text

	class Meta:
		ordering = ['-date', ]
		verbose_name = _("Comment")
		verbose_name_plural = _("Comments")