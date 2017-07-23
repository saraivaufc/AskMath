# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

from competition.views import ChallengeListView, ChallengeDetailView, SolutionCreateView, SolutionUpdateView, SolutionDeleteView

urlpatterns = [
	url(_(r'^list$'), ChallengeListView.as_view(), name="challenge_list"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), ChallengeDetailView.as_view(), name="challenge_detail"),
	url(_(r'^(?P<challenge_slug>[-\w]+)/solution/add$'), SolutionCreateView.as_view(), name="challenge_solution_add"),
	url(_(r'^(?P<challenge_slug>[-\w]+)/solution/(?P<pk>[0-9]+)/update$'), SolutionUpdateView.as_view(), name="challenge_solution_update"),
	url(_(r'^(?P<challenge_slug>[-\w]+)/solution/(?P<pk>[0-9]+)/delete$'), SolutionDeleteView.as_view(), name="challenge_solution_delete"),
]