# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_migrate

class AuthenticationConfig(AppConfig):
	name = 'authentication'
	verbose_name = _("Authentication")

	def ready(self):
		from authentication.management import create_user_groups
		post_migrate.connect(create_user_groups, sender=self)