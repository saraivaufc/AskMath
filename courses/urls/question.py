# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from courses.views import QuestionDetailView

urlpatterns = [
	url(_(r'^answer$'), login_required(QuestionDetailView.as_view()), name="answer_question"),
]