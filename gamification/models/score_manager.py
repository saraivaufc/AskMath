# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class ScoreManager(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"))
	xp = models.PositiveIntegerField(verbose_name=_("XP"), default=0)
	rp = models.PositiveIntegerField(verbose_name=_("RP"), default=0)
	skill = models.PositiveIntegerField(verbose_name=_("Skill"), default=0)
	reputation = models.PositiveIntegerField(verbose_name=_("Reputation"), default=0)

	def up_xp(self, factor):
		self.xp += factor

	def down_xp(self, factor):
		self.xp -= factor

	def up_rp(self, factor):
		self.rp += factor

	def down_rp(self, factor):
		self.rp -= factor

	def up_skill(self, factor):
		self.skill += factor

	def up_reputation(self, factor):
		self.reputation += factor

	def down_reputation(self, factor):
		self.reputation -= factor
	
	def __unicode__(self):
		return str(self.user)

	class Meta:
		ordering = []
		verbose_name = _('Score Manager')
		verbose_name_plural = _('Scores Manager')