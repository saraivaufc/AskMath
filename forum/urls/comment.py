from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from forum.views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
	url(_(r'^add$'), login_required(CommentCreateView.as_view()), name="comment_add"),
	url(_(r'^(?P<pk>[0-9]+)/update$'), login_required(CommentUpdateView.as_view()), name="comment_update"),
	url(_(r'^(?P<pk>[0-9]+)/delete$'), login_required(CommentDeleteView.as_view()), name="comment_delete"),
]