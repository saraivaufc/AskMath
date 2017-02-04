# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib.admin import AdminSite

from .models import (SocialNetwork)
from .forms import (SocialNetworkForm)

class SocialNetworkAdmin(admin.ModelAdmin):
	form = SocialNetworkForm
	list_display = ('name', 'url')
	list_filter = ['sites']

admin.site.register(SocialNetwork, SocialNetworkAdmin)