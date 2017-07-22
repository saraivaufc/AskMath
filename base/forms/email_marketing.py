# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from authentication.models import User
from ..models import EmailMarketing

class EmailMarketingForm(forms.ModelForm):
	class Meta:
		model = EmailMarketing
		fields = ['subject', 'message', 'quantity']

	def save(self, commit=True):
		email = super(EmailMarketingForm, self).save(commit=False)
		email.save()
		counter = 0
		for user in  User.objects.filter(is_active=True, is_staff=False).order_by('?')[:email.quantity]:
			self.send_email(user)
			email.receivers.add(user)		
			counter += 1

		email.quantity = counter

		if commit:
			email.save()
		return email

	def send_email(self, user):
		subject = self.cleaned_data['subject']
		message = self.cleaned_data['message']

		template_name = "base/emails/email_marketing.html"
		from_email = settings.DEFAULT_FROM_EMAIL
		recipients = [user.email]

		context = {
			'user': user.get_full_name(),
			'subject': subject, 
			'message': message,
		}

		html_content = render_to_string(template_name, context)
		email = EmailMultiAlternatives(subject=subject, from_email=from_email, to=recipients)
		email.attach_alternative(html_content, "text/html")
		print html_content
		#email.send()