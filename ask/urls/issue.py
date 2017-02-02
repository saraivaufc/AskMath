from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

from ask.views import IssueListView

urlpatterns = [
	url(_(r'^list$'), IssueListView.as_view(), name="issue_list"),
]