# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django import forms

from django.core.urlresolvers import reverse_lazy
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


from ..models import Report

class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ['name', 'email', 'message','reply']

	def save(self, commit=True):
		report = super(ReportForm, self).save(commit=False)
		report.save()

		if report.reply and not commit:
			self.send_email(report)

		if commit:
			report.save()
		return report


	def send_email(self, obj):
		template_name = "base/emails/reply.html"
		
		subject = _('Feedback')
		text_content = _('This is an important message.')
		
		from_email = settings.DEFAULT_FROM_EMAIL
		recipients = [obj.email]

		context = {
			'name': obj.name,
			'email': obj.email,
			'message': obj.message,
			'reply': obj.reply,
		}

		html_content = render_to_string(template_name, context)
		email = EmailMultiAlternatives(subject, text_content, from_email, recipients)
		email.attach_alternative(html_content, "text/html")
		print html_content
		#email.send()