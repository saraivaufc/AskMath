from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from .views import PostListView, PostByCategoryListView, PostDetailView

urlpatterns = [
	url(r'^$', PostListView.as_view(), name="post_list"),
	url(_(r'^post/(?P<slug>[-\w]+)/list$'), PostByCategoryListView.as_view(), name="post_list"),
	url(_(r'^post/(?P<slug>[-\w]+)/detail$'), PostDetailView.as_view(), name="post_detail"),
]