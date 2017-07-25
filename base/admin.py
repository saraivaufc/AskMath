# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import AdminSite
from django.utils import timezone
from django.conf import settings

from .models import (SocialNetwork, Report, EmailMarketing)
from .forms import (SocialNetworkForm, ReportForm, EmailMarketingForm)
from base import settings as local_settings

class SocialNetworkAdmin(admin.ModelAdmin):
	form = SocialNetworkForm
	list_display = ('name', 'url', 'creation')
	list_filter = ['sites']
	search_fields = ['name', ]

class ReportAdmin(admin.ModelAdmin):
	form = ReportForm
	list_display = ('name', 'email', 'solved_in', 'solved_by', 'last_modified')
	list_filter = ['solved_in', 'solved_by', 'last_modified',]
	search_fields = ['name','email', 'message']

	def save_model(self, request, obj, form, change):
		form.instance.solved_in = timezone.now()
		form.instance.solved_by = request.user
		form.save()

class EmailMarketingAdmin(admin.ModelAdmin):
	form = EmailMarketingForm
	model = EmailMarketing
	list_display = ('subject', 'message', 'quantity', 'creation',)
	list_filter = ['creation', ]
	search_fields = ['subject','message',]
	filter_horizontal = ['receivers']

admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(EmailMarketing, EmailMarketingAdmin)

admin.site.site_header = _("%(site_name)s - Administration") % {'site_name': local_settings.SITE_NAME}
admin.site.site_title = _("%(site_name)s - Site Administration") % {'site_name': local_settings.SITE_NAME}
admin.site.index_title = _("Applications")
