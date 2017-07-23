# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from courses.views import LessonListView, LessonFinishedView

urlpatterns = [
	url(_(r'^list$'), LessonListView.as_view(), name="lesson_list"),
	url(_(r'^(?P<slug>[-\w]+)/finished$'), login_required(LessonFinishedView.as_view()), name="lesson_finished"),
]