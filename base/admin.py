# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib.admin import AdminSite

from .models import (SocialNetwork)
from .forms import (SocialNetworkForm)

class SocialNetworkAdmin(admin.ModelAdmin):
	form = SocialNetworkForm
	list_display = ('name', 'url', 'created_by', 'last_modified')
	list_filter = ['sites']
	search_fields = ['name', ]
	

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

admin.site.register(SocialNetwork, SocialNetworkAdmin)