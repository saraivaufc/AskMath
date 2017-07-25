# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

from courses.views import CourseListView, CourseDetailView

urlpatterns = [
	url(_(r'^$'), CourseListView.as_view(), name="course_list"),
	url(_(r'^(?P<slug>[-\w]+)$'), CourseDetailView.as_view(), name="course_detail"),
]