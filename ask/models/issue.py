# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.conf import settings

from ..utils.colors import get_color

import itertools

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('w', _('Withdrawn')),
)

class Issue(models.Model):
	slug = models.SlugField(help_text=_(u"A short label, generally used in URLs."), blank=True)
	name = models.CharField(verbose_name=_(u"Name"), max_length=255)
	icon = models.ImageField(verbose_name=_(u"Icon"), upload_to=settings.ISSUE_PHOTO_DIR, null=True, blank=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	color = models.CharField(max_length=20, default=get_color, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.name)
			for x in itertools.count(1):
				if not Issue.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Issue, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _(u'Issue')
		verbose_name_plural = _(u'Issues')