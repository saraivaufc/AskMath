from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

from forum.views import CategoryListView

urlpatterns = [
	url(r'^$', CategoryListView.as_view(), name="category_list"),
]