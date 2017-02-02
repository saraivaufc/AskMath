# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify

from ..utils.colors import get_color

import itertools

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('w', _('Withdrawn')),
)

class Lesson(models.Model):
	slug = models.SlugField(help_text=_(u"A short label, generally used in URLs."), blank=True)
	issues = models.ManyToManyField("Issue", verbose_name=_(u"Issues"), related_name='lesson_issues', blank=True)
	name = models.CharField(verbose_name=_(u"Name"), max_length=255)
	description = models.TextField(verbose_name=_(u"Description"))
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	requirements = models.ManyToManyField("Lesson", verbose_name=_(u"Requirements"), related_name='lesson_requirements', blank=True)
	questions = models.ManyToManyField("Question", verbose_name=_(u"Questions"), related_name='lesson_question', blank=True)
	color = models.CharField(max_length=20, default=get_color, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.name)
			for x in itertools.count(1):
				if not Lesson.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Lesson, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _(u'Lesson')
		verbose_name_plural = _(u'Lessons')