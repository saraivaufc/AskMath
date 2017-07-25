# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.conf import settings

from base import settings as local_settings

class SocialNetwork(models.Model):
	name = models.CharField(verbose_name=_("Name"), max_length=255)
	url = models.URLField(verbose_name=_("URL"))
	icon = models.ImageField(verbose_name=_("Icon"), upload_to=local_settings.SOCIAL_NETWORK_ICON_DIR)
	sites = models.ManyToManyField(Site)

	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ("name", )
		verbose_name = _('Social Network')
		verbose_name_plural = _('Social Networks')