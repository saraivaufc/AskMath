# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from base.utils.models import AutoSlugField

from ..utils.colors import get_color

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('r', _('Removed')),
)

class Lesson(models.Model):
	issues = models.ManyToManyField("Issue", verbose_name=_(u"Issues"), related_name='lesson_issues', blank=True)
	name = models.CharField(verbose_name=_(u"Name"), max_length=255)
	slug = AutoSlugField(populate_from="name", db_index=False, blank=True, unique=True)
	description = models.TextField(verbose_name=_(u"Description"))
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	requirements = models.ManyToManyField("Lesson", verbose_name=_(u"Requirements"), related_name='lesson_requirements', blank=True)
	questions = models.ManyToManyField("Question", verbose_name=_(u"Questions"), related_name='lesson_question', blank=True)
	videos = models.ManyToManyField("Video", verbose_name=_(u"Videos"), related_name='lesson_video', blank=True)
	color = models.CharField(max_length=20, default=get_color, blank=True)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"User"), blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		issue = self.issues.filter(status='p').first()
		return reverse_lazy('ask:lesson_detail', kwargs={'issue_slug': issue.slug, 'slug': self.slug})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _(u'Lesson')
		verbose_name_plural = _(u'Lessons')