# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class RankingManager(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"))
	
	def __unicode__(self):
		return self.user

	class Meta:
		ordering = []
		verbose_name = _(u'Ranking Manager')
		verbose_name_plural = _(u'Rankings Manager')