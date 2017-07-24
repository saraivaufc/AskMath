# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from courses.views import QuestionVerificationView

urlpatterns = [
	url(_(r'^(?P<pk>[0-9]+)/verification$'), QuestionVerificationView.as_view(), name="question_verification"),
]