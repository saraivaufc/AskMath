# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^challenge/'), include('competition.urls.challenge')),
]