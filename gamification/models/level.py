# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import hashlib

from gamification import settings as local_settings

class Level(models.Model):
	name = models.CharField(verbose_name=_("Name"), max_length=100)
	number = models.PositiveIntegerField(verbose_name=_("Number"), unique=True)
	image = models.ImageField(verbose_name=_("Image"), upload_to=local_settings.LEVEL_IMAGE_DIR)

	def save(self, *args, **kwargs):
		if not self.id and self.image:
			hash = hashlib.md5(self.image.read()).hexdigest()
			if self.image.name.find(hash) == -1:
				self.image.name = "".join((hash, ".", self.image.name.split(".")[-1]))
		super(Level, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['number']
		verbose_name = _('Level')
		verbose_name_plural = _('Levels')