# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

class Answer(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"User"), blank=True)
	lesson = models.ForeignKey('Lesson', verbose_name=_(u"Lesson"), blank=True)
	question = models.ForeignKey('Question', verbose_name=_(u"Question"), blank=True)
	choices = models.ManyToManyField('Choice', verbose_name=_(u"Choices"))
	correct = models.BooleanField(verbose_name=_("Correct"), default=False)
	exists = models.BooleanField(verbose_name=_("Exists"), default=True)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), related_name="answer_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "Casa"
		return u"{0} >> {1} >> {2}".format(self.user, self.question, self.date)

	class Meta:
		ordering = ("-last_modified",)
		verbose_name = _(u'Answer')
		verbose_name_plural = _(u'Answers')

from django.db.models.signals import post_save
from django.dispatch import receiver

def post_save_receiver(sender, instance, created, ** kwargs):
	Answer.objects.filter(user=instance.user, question=instance.question).exclude(id=instance.id).update(exists=False)

post_save.connect(post_save_receiver, sender=Answer)