# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(r'^$', RedirectView.as_view(url=reverse_lazy('ask:home'), permanent=False)),
	url(_(r'^index$'), TemplateView.as_view(template_name="ask/index.html"), name="home"),
	url(_(r'^api/'), include('ask.api.urls')),
	
	url(_(r'^issues/'), include('ask.urls.issue')),
	url(_(r'^issues/(?P<issue_slug>[-\w]+)/lessons/'), include('ask.urls.lesson')),
	url(_(r'^issues/(?P<issue_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/questions/'), include('ask.urls.question')),
	url(_(r'^issues/(?P<issue_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/videos/'), include('ask.urls.video')),
]