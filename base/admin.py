# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import AdminSite
from django.utils import timezone

from .models import (SocialNetwork, Report, )
from .forms import (SocialNetworkForm, ReportForm, )

class SocialNetworkAdmin(admin.ModelAdmin):
	form = SocialNetworkForm
	list_display = ('name', 'url', 'created_by', 'last_modified')
	list_filter = ['sites']
	search_fields = ['name', ]
	

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class ReportAdmin(admin.ModelAdmin):
	model = Report
	list_display = ('name', 'email', 'message', 'solved_in', 'solved_by', 'last_modified')
	list_filter = ['solved_in', 'solved_by', 'last_modified',]
	search_fields = ['name','email', 'message']
	actions = ['make_solved']

	def make_solved(self, request, queryset):
		rows_updated = queryset.update(solved_in=timezone.now(), solved_by=request.user)
		if rows_updated == 1:
			message_bit = _("1 story was")
		else:
			message_bit = _("%s stories were" % rows_updated)
		self.message_user(request, _("%s successfully marked as solved." % message_bit) )

	make_solved.short_description = _("Mark selected stories as solved")

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(Report, ReportAdmin)