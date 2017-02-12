# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from ask.views import VideoListView, VideoDetailView

urlpatterns = [
	url(_(r'^list$'), VideoListView.as_view(), name="video_list"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), VideoDetailView.as_view(), name="video_detail"),
]