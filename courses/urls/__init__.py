# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^$'), TemplateView.as_view(template_name="courses/index.html"), name="home"),
	url(_(r'^api/'), include('courses.api.urls')),
	url(_(r'^courses/'), include('courses.urls.course')),
	url(_(r'^courses/(?P<course_slug>[-\w]+)/lessons/'), include('courses.urls.lesson')),
	url(_(r'^courses/(?P<course_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/questions/'), include('courses.urls.question')),
	url(_(r'^courses/(?P<course_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/videos/'), include('courses.urls.video')),
]