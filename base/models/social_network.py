# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site
from django.conf import settings

class SocialNetwork(models.Model):
	name = models.CharField(verbose_name=_(u"Name"), max_length=255)
	url = models.URLField(verbose_name=_(u"URL"))
	icon = models.ImageField(verbose_name=_(u"Icon"), upload_to=settings.SOCIAL_NETWORK_ICON_DIR)
	sites = models.ManyToManyField(Site)
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _(u'Social Network')
		verbose_name_plural = _(u'Social Networks')