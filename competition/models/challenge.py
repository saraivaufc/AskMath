# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from base.utils.models import AutoSlugField

class Challenge(models.Model):
	DRAFT = 'd'
	PUBLISHED = 'p'
	REMOVED = 'r'
	STATUS_CHOICES = (
		(DRAFT, _('Draft')),
		(PUBLISHED, _('Published')),
		(REMOVED, _('Removed')),
	)
	SEVERE = 's'
	INTERMEDIATE = 'i'
	EASY = 'e'
	LEVEL_CHOICES = (
		(SEVERE, _('Severe')),
		(INTERMEDIATE, _('Intermediate')),
		(EASY, _('Easy')),
	)
	slug = AutoSlugField(populate_from="title", db_index=False, blank=True, unique=True)
	title = models.CharField(verbose_name=_("Title"), max_length=255)
	description = models.TextField(verbose_name=_("Description"))
	level = models.CharField(max_length=1, verbose_name=_("Difficult level"), choices=LEVEL_CHOICES)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Created by"), related_name="challenge_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse_lazy('competition:challenge_list', kwargs={'challenge_slug': self.slug})

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-creation']
		verbose_name = _(u'Challenge')
		verbose_name_plural = _(u'Challenges')

class Solution(models.Model):
	challenge = models.ForeignKey('competition.Challenge', verbose_name=_(u"Challenge"))
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"User"), related_name="answer_user", blank=True)	
	text = models.TextField(verbose_name=_(u"Text"))
	is_correct = models.BooleanField(verbose_name=_("Correct"), default=False)
	
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.text

	class Meta:
		ordering = ("-is_correct", "last_modified",)
		verbose_name = _(u'Solution')
		verbose_name_plural = _(u'Solutions')