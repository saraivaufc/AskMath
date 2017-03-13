# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Level(models.Model):
	name = models.CharField(verbose_name=_(u"Name"), max_length=100)
	number = models.PositiveIntegerField(verbose_name=_(u"Number"), unique=True)
	image = models.ImageField(verbose_name=_(u"Image"), upload_to=settings.LEVEL_IMAGE_DIR)
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['number']
		verbose_name = _(u'Level')
		verbose_name_plural = _(u'Levels')