# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Min
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .level import Level

class LevelManager(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"))
	level = models.ForeignKey('gamification.Level', verbose_name=_("Level"), blank=True)

	def up_level(self):
		if Level.objects.filter(number=self.level.number+1).exists():
			self.level = Level.objects.get(number=self.level+1)
			return True
		else:
			return False

	def save(self, * args, ** kwargs):
		if not self.id:
			self.level = Level.objects.first()
		return super(LevelManager, self).save(* args, ** kwargs)

	def __unicode__(self):
		return str(self.user)

	class Meta:
		ordering = []
		verbose_name = _('Level Manager')
		verbose_name_plural = _('Levels Manager')