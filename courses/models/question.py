# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .lesson import Lesson


class Introduction(models.Model):
	question = models.OneToOneField("courses.Question", verbose_name=_(u"QUestion"), null=True, blank=True)
	text = models.TextField(verbose_name=_(u"Introduction text"))
	creation = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text[:50]

	class Meta:
		ordering = ['creation']
		verbose_name = _(u'Introduction')
		verbose_name_plural = _(u'Introductions')

class Question(models.Model):
	position = models.IntegerField(verbose_name=_(u"Position"), null=True, blank=True)
	text = models.TextField(verbose_name=_(u"Question text"))
	help = models.CharField(verbose_name=_(u"Help text"), max_length=255, null=True, blank=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="question_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)

	def get_choices(self):
		return Choice.objects.filter(question=self)

	def get_answers(self):
		return Answer.objects.filter(question=self)

	def __unicode__(self):
		return self.text[:50]

	class Meta:
		ordering = ['position', 'creation']
		verbose_name = _(u'Question')
		verbose_name_plural = _(u'Questions')

class Choice(models.Model):
	question = models.ForeignKey('courses.Question', verbose_name=_('Question'))
	text = models.CharField(verbose_name=_(u"Choice text"), max_length=255)
	is_correct = models.BooleanField(verbose_name=_(u"Is correct"), default=False)
	creation = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

	class Meta:
		ordering = ['creation']
		verbose_name = _(u'Choice')
		verbose_name_plural = _(u'Choices')


class Answer(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"User"), blank=True)
	lesson = models.ForeignKey('courses.Lesson', verbose_name=_(u"Lesson"), blank=True)
	question = models.ForeignKey('courses.Question', verbose_name=_(u"Question"), blank=True)
	choices = models.ManyToManyField('courses.Choice', verbose_name=_(u"Choices"))
	is_correct = models.BooleanField(verbose_name=_("Is Correct"), default=False)
	exists = models.BooleanField(verbose_name=_("Exists"), default=True)
	creation = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return u"{0} >> {1} >> {2}".format(self.user, self.question, self.creation)

	class Meta:
		ordering = ("-creation",)
		verbose_name = _(u'Answer')
		verbose_name_plural = _(u'Answers')

def post_save_receiver(sender, instance, created, ** kwargs):
	Answer.objects.filter(user=instance.user, question=instance.question).exclude(id=instance.id).update(exists=False)

post_save.connect(post_save_receiver, sender=Answer)