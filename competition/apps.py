from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class CompetitionConfig(AppConfig):
	name = 'competition'
	verbose_name = _("Competition")

