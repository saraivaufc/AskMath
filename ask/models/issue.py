# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.conf import settings

from base.utils.models import AutoSlugField

from ..utils.colors import get_color

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('w', _('Withdrawn')),
)

class Issue(models.Model):
	name = models.CharField(verbose_name=_(u"Name"), max_length=255)
	slug = AutoSlugField(populate_from="name", db_index=False, blank=True, unique=True)
	icon = models.ImageField(verbose_name=_(u"Icon"), upload_to=settings.ISSUE_PHOTO_DIR, null=True, blank=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	color = models.CharField(max_length=20, default=get_color, blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _(u'Issue')
		verbose_name_plural = _(u'Issues')